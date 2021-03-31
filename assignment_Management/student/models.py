from django.db import models
from login.models import Student
from teacher.models import Course,Assignment

# Create your models here.
class StudentCourse(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None,related_name="student")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=None,related_name="course")
    class Meta:
        unique_together = ('student', 'course')

class Submission(models.Model):
    submission_id=models.AutoField(primary_key=True)
    submission_file=models.FileField(upload_to='submissions/',null=True)
    submission_assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,default=None,related_name="assignment")
    submission_student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None,related_name="submission_student")
    submission_marks=models.FloatField(null=True,default=None)
    submission_added_time=models.DateTimeField(default=None)