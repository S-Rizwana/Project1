from django.shortcuts import render,redirect,get_object_or_404
from jobseakerapp.models import *
from django.contrib import messages
from django.db.models.query import Q
from jobseakerapp.models import *
from django.core.paginator import Paginator




def admin_login(req):
    if req.method == "POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        if username == "admin" and password == "admin":
                    messages.success(req,'Successfully Login')
                    return redirect('admin_index')
        else:
                    messages.warning(req,'invalid login')
                    return redirect("admin_login")
    return render (req,'main/main-admin-login.html')

def admin_index(req):
    return render (req,'admin/admin-index.html')    


def admin_all_users(req):
    
    restrict=User.objects.filter(Q(user_otp_status='otp verified')|Q(user_otp_status='Accepted')|Q(user_otp_status='Restricted')).order_by('-user_id')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-allusers.html',{'restrict':post})

def change_status_users(req,user_id):
    change_status = get_object_or_404(User,user_id=user_id)
    if change_status.user_otp_status == 'Accepted':
        change_status.user_otp_status ="Restricted"
        messages.warning(req,'User Restricted')
    else:
        change_status.user_otp_status ="Accepted"
        messages.success(req,'User Approved')
          
    change_status.save(update_fields=["user_otp_status"])
    change_status.save()
    return redirect('admin_all_users')

def remove_users(req,user_id):
    remove = get_object_or_404(User,user_id=user_id)
    remove.delete()
    messages.error(req,'User Terminated')
    return redirect('admin_all_users')



# def change_status_users(req,user_id):
#     change_status = get_object_or_404(User,user_id=user_id)
#     if change_status.user_status == 'Accepted':
#         change_status.user_status ="Restricted"
#         messages.warning(req,'User Restricted')
#     else:
#         change_status.user_status ="Accepted"
#         messages.success(req,'User Approved')
          
#     change_status.save(update_fields=["user_status"])
#     change_status.save()
#     return redirect('admin_all_user')

# def remove_users(req,user_id):
#     remove = get_object_or_404(User,user_id=user_id)
#     remove.delete()
#     messages.error(req,'User Terminated')
#     return redirect('admin_all_user')






def admin_user_profile(req):

    restrict=User.objects.all().order_by('-user_id').exclude(user_otp_status='otp is pending')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-userprofile.html',{'restrict':post})
    
def admin_user_profile_view(req,user_id):
    profile = User.objects.get(user_id=user_id)
    return render (req,'admin/admin-user-profile-view.html',{'user':profile})
    
def admin_analysis_report(req):
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



    


    return render (req,'admin/admin-analysis-report.html',context)
    
def admin_feedback(req):
   
    
    restrict=Feedback.objects.all().order_by('-feed_id')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-feedback.html',{'restrict':post})
    
def admin_feedback_analysis(req):
    very_positive = Feedback.objects.filter(feedback_sentiment='Very Positive').count()
    positive = Feedback.objects.filter(feedback_sentiment='Positive').count()
    neutral = Feedback.objects.filter(feedback_sentiment='Neutral').count()
    negative = Feedback.objects.filter(feedback_sentiment='Negative').count()
    very_negative = Feedback.objects.filter(feedback_sentiment='Very Negative').count()
    context = {
              'i':very_positive,
              'j':positive,
              'k':neutral,
              'l':negative,
              'm':very_negative,
              
          } 
    return render (req,'admin/admin-feedback-analysis.html',context)