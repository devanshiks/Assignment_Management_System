from django.db import models
from login.models import Teacher

# Create your models here.
class Course(models.Model):
    course_id=models.CharField(max_length=10,primary_key=True)
    course_name=models.CharField(max_length=30)
    course_branch=models.CharField(max_length=50)
    course_credit=models.DecimalField(decimal_places=2,max_digits=5)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Assignment(models.Model):
    assignment_id=models.AutoField(primary_key=True)
    assignment_name=models.CharField(max_length=50)
    assignment_created=models.DateTimeField(default=None)
    assignment_due_date=models.DateTimeField(default=None)
    assignment_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    assignment_teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    assignment_file=models.FileField(upload_to='files/',null=True)