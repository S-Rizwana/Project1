"""webscraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as mainapp_views
from adminapp import views as adminapp_views
from jobseakerapp import views as jobseakerapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
#mainapp views
    path('', mainapp_views.main_index,name='main_index'),
    path('main-about', mainapp_views.main_about,name='main_about'),
    path('main-contact', mainapp_views.main_contact,name='main_contact'),
#admin views    
    path('admin-login', adminapp_views.admin_login,name='admin_login'),
    path('admin-index', adminapp_views.admin_index,name='admin_index'),
    path('admin-all-users', adminapp_views.admin_all_users,name='admin_all_users'),
    path('admin-user-profile', adminapp_views.admin_user_profile,name='admin_user_profile'),
    path('admin-user-profile-view/<int:user_id>/', adminapp_views.admin_user_profile_view,name='admin_user_profile_view'),
    path('admin-analysis-report', adminapp_views.admin_analysis_report,name='admin_analysis_report'),
    path('admin-feedback', adminapp_views.admin_feedback,name='admin_feedback'),
    path('admin-feedback-analysis', adminapp_views.admin_feedback_analysis,name='admin_feedback_analysis'),
    
    path('change-status-users/<int:user_id>/',adminapp_views.change_status_users,name="change_status_users"),
    path('remove-users/<int:user_id>/',adminapp_views.remove_users,name="remove_users"),
#jobseaker views
    path('jobseaker-login', jobseakerapp_views.jobseaker_login,name='jobseaker_login'),
    path('jobseaker-register', jobseakerapp_views.jobseaker_register,name='jobseaker_register'),
    path('otp-verification', jobseakerapp_views.otp_verification,name='otp_verification'),
    path('otp-validation/<str:otp>', jobseakerapp_views.otp_validation,name='otp_validation'),


    path('jobseaker-index', jobseakerapp_views.jobseaker_index,name='jobseaker_index'),
    path('jobseaker-analyze-job-post', jobseakerapp_views.jobseaker_analyze_job_post,name='jobseaker_analyze_job_post'),
    path('jobseaker-job-details-page', jobseakerapp_views.jobseaker_job_details_page,name='jobseaker_job_details_page'),
    path('jobseaker-survey', jobseakerapp_views.jobseaker_survey,name='jobseaker_survey'),
    path('jobseaker-analysis-report', jobseakerapp_views.jobseaker_analysis_report,name='jobseaker_analysis_report'),
    path('jobseaker-feedback', jobseakerapp_views.jobseaker_feedback,name='jobseaker_feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

