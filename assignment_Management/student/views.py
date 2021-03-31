from django.shortcuts import render
from django.shortcuts import render
from teacher.models import Course,Assignment
from login.models import Student, Teacher
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.db.models.fields import DateTimeField
import datetime
import cgi,os,sys
import cgitb
from django.views.decorators.clickjacking import xframe_options_exempt
from student.models import StudentCourse,Submission

global ChangedState
# Create your views here.
def StudentHomePage(request):
    #Pending Assignments of students in enrolled courses
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        print(loggedin_user)
        current_user=Student.objects.get(stu_email=loggedin_user)
        print(current_user)
        #object of students who enrolled in a course
        enrolled = StudentCourse.objects.filter(student=current_user)
        print("enrolled courses:", enrolled)
        #list of courses objects from the enrolled queryset
        course=[]
        for i in enrolled:
            course.append(i.course)
            print("courses are: ",course)
        assignment=[]
        for j in course:
            #checking for assignments in 'j' particular course
            a = Assignment.objects.filter(assignment_course=j)
            print("assignment in courses:",a)
            # a will give queryset, but we want the fields which are inside the objects, so first we wil extract the objects
            for i in a:
                # now there are only objects and not queryset, so fields can be easily extracted
                assignment.append(i)
                print("assignment in courses:",i)
        print(assignment)

        submitted=[]
        pending=[]
        for i in assignment:
            s = Submission.objects.filter(submission_student=current_user,submission_assignment=i)
            print(s)
            if s.exists():
                for j in s:
                    submitted.append(j)
            else:
                pending.append(i)

        print("submitted list:",submitted)
        print("Pending list:", pending)   
        return render(request, 'StudentHome.html', {'pending':pending,'submitted':submitted})

def StudentCourseList(request): #show new courses as well as enrolled courses
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user=Student.objects.get(stu_email=loggedin_user)
        sc= StudentCourse.objects.filter(student=current_user)
        courses=[]
        for i in sc:
            courses.append(i.course)
        print(courses)
        user_branch=current_user.stu_branch
        cor=Course.objects.filter(course_branch=user_branch)
        print(cor)
        enrolled=[]
        newcourse=[]
        # comparing two list cor and courses which may be of different sizes
        for i in range(len(cor)):
            if cor[i] not in courses:
                newcourse.append(cor[i])
                print(i)
            else:
                enrolled.append(cor[i])
                print(i)
            print("enrolled courses are: ",enrolled)
            print("new courses are: ",newcourse)
        return render(request, 'StudentCourseList.html', {'enrolled':enrolled, 'newcourse':newcourse})

def AddStudentCourse(request): #enroll
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user=Student.objects.get(stu_email=loggedin_user)
        getid=request.POST.get('id','')
        course=Course.objects.get(course_id=getid)
        sc = StudentCourse(student=current_user, course=course)
        sc.save()
        return StudentCourseList(request)
    
def RemoveStudentCourse(request): #unenroll
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        course=Course.objects.get(course_id=getid)
        sc = StudentCourse.objects.get(course=course)
        sc.delete()
        msg="Unenrolled Successfully"
        return StudentCourseList(request)
    
def AddSubmissionPage(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user=Student.objects.get(stu_email=loggedin_user)
        getid=request.POST.get('id','')
        a=Assignment.objects.get(assignment_id=getid)
    return render(request,'AddSubmission.html', {'a':a})

def AddSubmission(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user=Student.objects.get(stu_email=loggedin_user)
        getid=request.POST.get('id','')
        print("id is:",getid)
        assignment=Assignment.objects.get(assignment_id=getid)
        print(assignment)
        submission_file=request.FILES['submission_file']
        submission_added_time=datetime.datetime.now()  
        s = Submission(submission_file=submission_file, submission_assignment=assignment, submission_student=current_user,
        submission_added_time=submission_added_time)
        s.save()
        print("Submission uploaded successfully")
    return StudentHomePage(request)



