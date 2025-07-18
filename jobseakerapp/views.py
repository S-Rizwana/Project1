from django.shortcuts import render,redirect,get_object_or_404
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd
from jobseakerapp.models import *
from textblob import TextBlob
import random
from django.contrib import messages

def jobseaker_login(req):
    if req.method == 'POST':
            email = req.POST.get('email')
            password = req.POST.get('password')
            print(email,password)
            try:
                        user = User.objects.get(
                        user_email=email, user_password=password)
                        req.session['user_id'] = user.user_id
                        if user.user_otp_status == 'otp verified' or user.user_otp_status == 'Accepted':
                                messages.success(req, 'Successfully Login')
                                return redirect('jobseaker_index')
                        elif user.user_otp_status == 'otp is pending':

                                # messages.warning(req, 'Your request is in pending, please wait for until acceptance')
                                return redirect('otp_verification')

                        elif user.user_otp_status == 'Restricted':
                                messages.warning(req, 'Your request is Restricted, so you cannot login')
                                return redirect('jobseaker_login')    
                                
            except:
                        print('hi')
                        messages.warning(req, 'invalid login')
                        return redirect('jobseaker_login')
                        
    return render(req,'main/main-user-login.html')
    
def jobseaker_register(req):
    if req.method == 'POST' and req.FILES["pic"]:
                    username = req.POST.get("username")
                    email = req.POST.get("email")
                    password = req.POST.get("password")
                    contact = req.POST.get("contact")
                    addresss = req.POST.get("addresss")
                    image = req.FILES["pic"]
                    gen_otp = random.randint(0000, 9999)
                    print(gen_otp)
                    User.objects.create( user_username=username , user_email=email , user_password=password , user_contact=contact , user_addresss=addresss  , user_image=image ,user_otp=gen_otp)
                    url = "https://www.fast2sms.com/dev/bulkV2"
                    message = ' Dear {}. Welcome to Reveal. Here is your One Time Validation {}. For Your First Time Login'.format(username,gen_otp)
                    numbers = contact
                    payload = f'sender_id=FTWSMS&message={message}&language=english&route=v3&numbers={numbers}'
                    headers = {
                    'authorization': "xZIssgvbBl4hSeai7mMebAMxcusK4BbhQZGO3v1O0ZlAUjuRFWhLAR5hA2SK",
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache",
                    }
                    response = requests.request("POST", url, data=payload, headers=headers)
                    print(response.text,'heloooooo')
                    messages.success(req, 'Successfully Registered')
    return render(req,'main/main-user-register.html')
        

def otp_verification(req):
    
 
    if req.method == 'POST':
        otp1 = req.POST.get('otp1')
        otp2 = req.POST.get('otp2')
        otp3 = req.POST.get('otp3')
        otp4 = req.POST.get('otp4')
        otp = otp1+otp2+otp3+otp4
        # print(user_otp ,type(user_otp), ' otppppppppppppppppppppppppppppppp')
        return redirect('otp_validation',otp)

    

    return render(req,'main/main-otp-verification.html')

def otp_validation(req,otp):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    if user.user_otp == otp:
        ver_otp = get_object_or_404(User,user_id=user_id)
        ver_otp.user_otp_status ="otp verified"
        ver_otp.save(update_fields=["user_otp_status"])
        ver_otp.save()
        messages.success(req, 'OTP Verified Successfully')

        return redirect('jobseaker_index')
    else:
        messages.warning(req, 'Invalid OTP')

        return redirect('otp_verification')

    return redirect('otp_validation')


def jobseaker_index(req):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    return render(req,'jobseaker/jobseaker-index.html')

        
def jobseaker_analyze_job_post(req):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    if req.method == 'POST':
        url=req.POST.get('url')
        URL.objects.create(url=url,user_url=user)
        return redirect('jobseaker_job_details_page')
    return render(req,'jobseaker/jobseaker-analyze-job-post.html')
            

    
def jobseaker_job_details_page(req):
    user_id = 11  # Hardcoded for testing; replace with req.session.get('user_id')
    
    try:
        user = User.objects.get(user_id=user_id)  # Fetch user
        url_record = URL.objects.filter(user_url=user_id).order_by('-url_id').first()  # Get the latest URL
        
        if not url_record:
            messages.warning(req, 'No URL found for this user.')
            return redirect('jobseaker_analyze_job_post')

        url = url_record.url.strip().rstrip("\\")  # Clean URL
        print(f"Fetching URL: {url}")  # Debugging to ensure it's not always the same

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            messages.warning(req, 'Failed to fetch the job page.')
            return redirect('jobseaker_analyze_job_post')

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract job details safely
        job_title = soup.select_one("span.profile_on_detail_page")
        company_name = soup.select_one("a.link_display_like_text.view_detail_button")
        company_website = soup.select_one("div.text-container.website_link a")
        location = soup.select_one("p#location_names")
        job_details_section = soup.select_one("div.internship_details")
        skills_required = soup.select_one("div.round_tabs_container")
        salary = soup.select_one("div.text-container.salary_container")
        hiring_activity = soup.select_one("div.activity_section")

        # Extract text values with fallback
        job_title = job_title.get_text(strip=True) if job_title else "Not Found"
        company_name = company_name.get_text(strip=True) if company_name else "Not Found"
        company_website_text = company_website.get_text(strip=True) if company_website else "No Website"
        company_website_link = company_website['href'] if company_website else ""
        location = location.get_text(strip=True) if location else "Not Available"
        job_details = job_details_section.get_text(strip=True) if job_details_section else "Details Not Found"
        skills_required = skills_required.get_text(strip=True) if skills_required else "Not Mentioned"
        salary = salary.get_text(strip=True) if salary else "Not Mentioned"
        hiring_activity = hiring_activity.get_text(strip=True) if hiring_activity else "No Activity Data"

# Fake job detection logic
        if "Immediately" in job_details and "Work from home" in location:
            status = "Fake"
        elif not company_website_link:
            status = "Fake"
        else:
            status = "Genuine"


        print(f"Job Title: {job_title}, Company: {company_name}, Status: {status}")  # Debugging

        context = {
            'status': status,
            'job_title': job_title,
            'company': company_name,
            'company_website_text': company_website_text,
            'company_website_link': company_website_link,
            'company_location': location,
            'job_details': job_details,
            'skills_required': skills_required,
            'salary': salary,
            'hiring_activity': hiring_activity,
        }

    except Exception as e:
        print("Error:", e)
        messages.warning(req, 'Invalid URL or Parsing Error.')
        return redirect('jobseaker_analyze_job_post')

    return render(req, 'jobseaker/jobseaker-job-details-page.html', context)


        
def jobseaker_survey(req):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    if req.method == 'POST':
        option1 = req.POST.get("radio1")
        option2 = req.POST.get("radio2")
        option3 = req.POST.get("radio3")
        option4 = req.POST.get("radio4")
        option5 = req.POST.get("radio5")
        option6 = req.POST.get("radio6")
        option7 = req.POST.get("radio7")
        option8 = req.POST.get("radio8")
        option9 = req.POST.get("radio9")
        option10 = req.POST.get("radio10")
        option11 = req.POST.get("radio11")
        option12 = req.POST.get("radio12")
        Survey.objects.create(user_id=user,option1=option1,option2=option2,option3=option3,option4=option4,option5=option5,option6=option6,option7=option7,option8=option8,option9=option9,option10=option10,option11=option11,option12=option12)
        print(option1,option2,option3,option4,option5,option6,option7,option8,option9,option10,option11,option12)
        messages.success(req, 'Survey Submitted Successfully')
        
    return render(req,'jobseaker/jobseaker-survey.html')
            

        
def jobseaker_analysis_report(req):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    Aa = Survey.objects.filter(option1 = 'Computer Software').count()
    Ab = Survey.objects.filter(option1 = 'Information Technology and Services').count()
    Ac = Survey.objects.filter(option1 = 'Internet').count()
    Ad = Survey.objects.filter(option1 = 'Marketing and Advertising').count()
    Ae = Survey.objects.filter(option1 = 'Education Management').count()
    Ba = Survey.objects.filter(option2 = 'Full Time').count()
    Bb = Survey.objects.filter(option2 = 'Part Time').count()
    Bc = Survey.objects.filter(option2 = 'Intern').count()
    Bd = Survey.objects.filter(option2 = 'Contract').count()
    Ca = Survey.objects.filter(option3 = 'Yes').count()
    Cb = Survey.objects.filter(option3 = 'No').count()
    Da = Survey.objects.filter(option4 = 'Fresher').count()
    Db = Survey.objects.filter(option4 = 'Associate').count()
    Dc = Survey.objects.filter(option4 = 'Internship').count()
    Dd = Survey.objects.filter(option4 = 'Mid Senior Level').count()
    De = Survey.objects.filter(option4 = 'Not Applicable').count()
    Ea = Survey.objects.filter(option5 = "Bachelor's Degree").count()
    Eb = Survey.objects.filter(option5 = 'High School').count()
    Ec = Survey.objects.filter(option5 = "Master's Degree").count()
    Ed = Survey.objects.filter(option5 = 'Associate Degree').count()
    Ee = Survey.objects.filter(option5 = 'Unspecified').count()
    Fa = Survey.objects.filter(option6 = 'Sales Executive').count()
    Fb = Survey.objects.filter(option6 = 'Web DEveloper').count()
    Fc = Survey.objects.filter(option6 = 'Project Intern').count()
    Fd = Survey.objects.filter(option6 = 'Research associate').count()
    Fe = Survey.objects.filter(option6 = 'Product Manager').count()
    Ga = Survey.objects.filter(option7 = 'E-mail').count()
    Gb = Survey.objects.filter(option7 = 'Social Media').count()
    Gc = Survey.objects.filter(option7 = 'Online Website').count()
    Gd = Survey.objects.filter(option7 = 'College').count()
    Ge = Survey.objects.filter(option7 = 'Super Set').count()
    Ha = Survey.objects.filter(option8 = 'Less Than 1000k').count()
    Hb = Survey.objects.filter(option8 = '1000k to 5000k').count()
    Hc = Survey.objects.filter(option8 = '5000k to 10,000k').count()
    Hd = Survey.objects.filter(option8 = '10,000k Above').count()
    Ia = Survey.objects.filter(option9 = 'Yes').count()
    Ib = Survey.objects.filter(option9 = 'No').count()
    Ja = Survey.objects.filter(option10 = 'Personal Details').count()
    Jb = Survey.objects.filter(option10 = 'Credit Card Details').count()
    Jc = Survey.objects.filter(option10 = 'Documents').count()
    Jd = Survey.objects.filter(option10 = 'Photo and Media').count()
    Je = Survey.objects.filter(option10 = 'Money').count()
    Ka = Survey.objects.filter(option11 = 'Yes').count()
    Kb = Survey.objects.filter(option11 = 'No').count()
    Kc = Survey.objects.filter(option11 = 'Nill').count()
    La = Survey.objects.filter(option12 = 'Whatsapp').count()
    Lb = Survey.objects.filter(option12 = 'Facebook').count()
    Lc = Survey.objects.filter(option12 = 'Instagram').count()
    Ld = Survey.objects.filter(option12 = 'Indeed').count()
    Le = Survey.objects.filter(option12 = 'Linkedin').count()

    context = {
        'Aa':Aa ,
        'Ab':Ab ,
        'Ac':Ac ,
        'Ad':Ad ,
        'Ae':Ae ,
        'Ba':Ba ,
        'Bb':Bb ,
        'Bc':Bc ,
        'Bd':Bd ,
        'Ca':Ca ,
        'Cb':Cb ,
        'Da':Da ,
        'Db':Db ,
        'Dc':Dc ,
        'Dd':Dd ,
        'De':De ,
        'Ea':Ea ,
        'Eb':Eb ,
        'Ec':Ec ,
        'Ed':Ed ,
        'Ee':Ee ,
        'Fa':Fa ,
        'Fb':Fb ,
        'Fc':Fc ,
        'Fd':Fd ,
        'Fe':Fe ,
        'Ga':Ga ,
        'Gb':Gb ,
        'Gc':Gc ,
        'Gd':Gd ,
        'Ge':Ge ,
        'Ha':Ha ,
        'Hb':Hb ,
        'Hc':Hc ,
        'Hd':Hd ,
        'Ia':Ia ,
        'Ib':Ib ,
        'Ja':Ja ,
        'Jb':Jb ,
        'Jc':Jc ,
        'Jd':Jd ,
        'Je':Je ,
        'Ka':Ka ,
        'Kb':Kb ,
        'Kc':Kc ,
        'La':La ,
        'Lb':Lb ,
        'Lc':Lc ,
        'Ld':Ld ,
        'Le':Le 

    }



    




    return render(req,'jobseaker/jobseaker-analysis-report.html',context)
            

        
def jobseaker_feedback(req):
    user_id = req.session['user_id']
    user = User.objects.get(user_id=user_id)
    if req.method == 'POST' :
        desc = req.POST.get("feedback")
        rating = req.POST.get("rating")
        print(desc, rating)
        user_id = req.session['user_id']
        user = User.objects.get(pk=user_id)
        if not rating:
                    messages.info(req, 'Please Give rating')            
                    return redirect('jobseaker_feedback')
        analysis = TextBlob(desc)
        senti = ''
        if analysis.polarity >= 0.5:
                    senti = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
                    senti = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
                    senti = 'Negative'
        elif analysis.polarity < -0.5:
                    senti = 'Very Negative'
        else:
                    senti = 'Neutral'
        print(senti, 'sentiment')
        print(desc)
        Feedback.objects.create(feed_desc=desc, feed_rating=rating,feedback_sentiment=senti,feedback_user=user)
        messages.success(req,'Feedback Submitted') 
    return render(req,'jobseaker/jobseaker-feedback.html')
            

    

        