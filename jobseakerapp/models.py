from django.db import models

# Create your models here.



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_username = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=15)
    user_addresss = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='images/user')
    user_otp_status = models.CharField(default='otp is pending', max_length=50)
    user_otp = models.CharField(max_length=10,null=True)

    class Meta:
        db_table = 'User_Details'

class URL(models.Model):
    url_id = models.AutoField(primary_key=True)
    user_url = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_url')
    url=models.TextField()

    class Meta:
        db_table = 'URL_Deatils'


class Survey(models.Model):

    survey_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    option1 = models.CharField(max_length=50,null=True)
    option2 = models.CharField(max_length=50,null=True)
    option3 = models.CharField(max_length=50,null=True)
    option4 = models.CharField(max_length=50,null=True)
    option5 = models.CharField(max_length=50,null=True)
    option6 = models.CharField(max_length=50,null=True)
    option7 = models.CharField(max_length=50,null=True)
    option8 = models.CharField(max_length=50,null=True)
    option9 = models.CharField(max_length=50,null=True)
    option10 = models.CharField(max_length=50,null=True)
    option11 = models.CharField(max_length=50,null=True)
    option12 = models.CharField(max_length=50,null=True)
    
    class Meta:
        db_table = 'survey_details'


class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    feed_desc = models.TextField()
    feed_rating = models.CharField(default='0', max_length=100)
    feedback_sentiment = models.CharField(max_length=50)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feedbacks')

    class Meta:
        db_table = 'feedback_details'