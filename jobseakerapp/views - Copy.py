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
    
    #user_id = req.session['user_id']
    user_id = 21
    user = User.objects.get(user_id=user_id)
    try:
    
        url_link = URL.objects.filter(user_url=user_id).order_by('-url_id')[0:1]
        for i in url_link:
            
            url = i.url

        page = requests.get(url)

        soup = BeautifulSoup(page.content,'html.parser')

        name=soup.find('div', class_="detail_view")


        title=soup.find('span', attrs={'class':'profile_on_detail_page'}).get_text().strip()
        company=soup.find('a', attrs={'class':'link_display_like_text view_detail_button'}).get_text().strip()

        details_companylinksrc=soup.find('div', attrs={'class':'text-container website_link'})

        try:
            details_companylinktext = details_companylinksrc.find('a').get_text().strip()
            details_companylink = details_companylinksrc.find('a').get('href').strip()
        except:
            details_companylinktext = 'No Website Link Available'
            details_companylink = ''




        # details_companylinktext = details_companylinksrc.find('a').get_text().strip()

        logosrc=soup.find('div', attrs={'class':'internship_logo'})
        # logo = logosrc.find('img').get('src').strip()
        location=soup.find('p', attrs={'id':'location_names'}).get_text().strip()

        internshipdetails=soup.find('div', attrs={'class':'other_detail_item_row'}).get_text().strip()
        tags=soup.find('div', attrs={'class':'tags_container_outer'}).get_text().strip()
        details=soup.find('div', attrs={'class':'internship_details'})
        details_about_company_title=soup.find('div',attrs={'class':'section_heading heading_5_5'}).get_text().strip()
        details_about_company=soup.find('div',attrs={'class':'text-container about_company_text_container'}).get_text().strip()
        details_company_activity=soup.find('div',attrs={'class':'activity_section'}).get_text().strip()
        candidates = soup.find('div',attrs={'class':'activity_container'})
        candidates_hired = candidates.find_all('div',attrs={'class':'text body-main'})[-1].get_text()
        
        

        print(details_companylink,'linkkkkk')

        print(candidates_hired,'hired',type(candidates_hired))
        job_details=""
        for i in details.find_all('div',attrs={'class':"text-container"})[2:3]:
        # print(i) 
            job_details += i.get_text().strip()
        openings=0
        for j in  details.find_all('div',attrs={'class':"text-container"})[-1]:
            
            openings += int(j)
        skills_required = soup.find('div',attrs={'class':'round_tabs_container'}).get_text().strip()
        salary = soup.find('div',attrs={'class':'text-container salary_container'}).get_text().strip()
        # print(job_details,tags,details_company_activity)
        
        if 'Immediately' in internshipdetails and 'Work from home' in location:
            status = 'Fake'
        elif details_companylink == '':
            status = 'Fake'
        elif openings >= 50 :
            status = 'Fake'
        else:
            status = 'Genuine'
        print(status)
        context = {
        'status':status,
        'job_details':job_details,
        'logosrc':logosrc,
        'job_title':title,
        'company':company,
        'companylinktext':details_companylinktext,
        'company_website_link':details_companylink,
        # 'company_logo':logo,
        'company_location':location,
        'internship_deatils':internshipdetails,
        'company_posted_tags':tags,
        'about_company_title':details_about_company_title,
        'about_company':details_about_company,
        'company_hiring_activity':details_company_activity,
        'skills_required':skills_required,
        'salary':salary,
        'openings':openings}
    except:
        context=None
        messages.warning(req, 'Invalid URL')
        return redirect('jobseaker_analyze_job_post')


    


    return render(req,'jobseaker/jobseaker-job-details-page.html',context)
        
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
            

    

        