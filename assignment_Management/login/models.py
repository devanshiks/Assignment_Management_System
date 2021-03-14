from django.db import models

# Create your models here
class Teacher(models.Model):
    teach_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    teach_name=models.CharField(max_length=30)
    teach_dob=models.DateTimeField()
    teach_gender=models.CharField(max_length=10)
    teach_address=models.CharField(max_length=100,help_text = 'write your add')
    teach_city=models.CharField(max_length=20)
    teach_state=models.CharField(max_length=20)
    teach_zip=models.CharField(max_length=6)
    teach_mobile_no=models.CharField(max_length=10)
    teach_image=models.ImageField(upload_to='teacher_pics',blank=True)
  
class Student(models.Model):
    stu_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    stu_name=models.CharField(max_length=30)
    stu_dob=models.DateTimeField()
    stu_gender=models.CharField(max_length=10)
    stu_sem=models.IntegerField()
    stu_branch=models.CharField(max_length=6)
    stu_address=models.CharField(max_length=100,help_text = 'write your add')
    stu_city=models.CharField(max_length=20)
    stu_state=models.CharField(max_length=20)
    stu_zip=models.CharField(max_length=6)
    stu_mobile_no=models.CharField(max_length=10)
    stu_image=models.ImageField(upload_to='stu_pics',blank=True)
  