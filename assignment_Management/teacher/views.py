
from django.shortcuts import render
from teacher.models import Course,Assignment
from student.models import StudentCourse, Submission
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
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        cor = Course.objects.filter(teacher=current_user)
        assignment=Assignment.objects.filter(assignment_teacher=current_user)
        if assignment.exists():
            paginator = Paginator(assignment,4)
            page = request.GET.get('page', 1)
            try:
                assignment = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            return render(request, 'Home.html',{'assignment':assignment,'cor':cor})
    return render(request, 'Home.html',{'cor':cor, 'assignment':assignment})

def CoursesPage(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        course = Course.objects.filter(teacher=current_user)
    return render(request, 'Courses.html', {'course':course})

def AddCourse(request):
    if request.user.is_authenticated:
        course_id=request.POST.get('course_id','')
        course_name=request.POST.get('course_name','')
        course_branch=request.POST.get('course_branch','')
        course_credit=request.POST.get('course_credit','')
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        c = Course(course_id=course_id, course_name=course_name, course_branch=course_branch, course_credit=course_credit, 
        teacher=current_user)
        c.save()
        course = Course.objects.filter(teacher=current_user)
    return render(request, 'Courses.html', {'course':course})

def AddAssignment(request):
    if request.user.is_authenticated:
        assignment_name=request.POST.get('assignment_name','')
        assignment_course=request.POST.get('assignment_course','')
        assignment_due_date=request.POST.get('assignment_due_date','')
        assignment_file=request.FILES['assignment_file']
        assignment_created=datetime.datetime.now()  
        loggedin_user=request.user.username
        teacher=Teacher.objects.get(teach_email=loggedin_user)
        course=Course.objects.get(course_name=assignment_course)
        assign=Assignment(assignment_name=assignment_name,assignment_due_date=assignment_due_date,assignment_created=assignment_created,
        assignment_file=assignment_file,assignment_teacher=teacher, assignment_course=course)
        assign.save()
        assignment=Assignment.objects.filter(assignment_teacher=teacher)
        cor=Course.objects.filter(teacher=teacher)
        msg="Assignment Added Successfully"
    return render(request, 'Home.html', {'cor':cor,'course': course, 'assignment':assignment, 'msg':msg})

def StudentDetailsPage(request): # Enrolled Students and their Submissions
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        # students enrolled in courses added by loggedin teacher
        course = Course.objects.filter(teacher=current_user)
        studentcourse=[]
        for i in course:
            sc = StudentCourse.objects.filter(course=i)
            if sc.exists():
                for j in sc:
                    studentcourse.append(j)
        print("studentcourse:",studentcourse)
        paginator = Paginator(studentcourse,4)
        page = request.GET.get('page', 1)
        try:
            studentcourse = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'StudentDetails.html', {'studentcourse':studentcourse})

def ViewAssignmentSubmission(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        assign_id=request.POST.get('id','')
        a = Assignment.objects.get(assignment_id=assign_id)
        print(a)
        sc = Submission.objects.filter(submission_assignment=a)
        print(sc)
        sc1 = []
        for i in sc:
            sc1.append(i)
        print(sc1)
    return render(request, 'ViewAssignmentSubmission.html',{'sc1':sc1, 'assign_id':assign_id})

def ViewStudentSubmission(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user= Teacher.objects.get(teach_email=loggedin_user)
        getid=request.POST.get('id','')
        print(getid)
        cor = Course.objects.get(course_id=getid)
        print(cor)
        getemail=request.POST.get('em','')
        stu=Student.objects.get(stu_email=getemail)
        sub=[]
        s = Submission.objects.filter(submission_student=stu)
        for i in s:
            if i.submission_assignment.assignment_course == cor:
                sub.append(i)
        print("Submissions",sub)
        # students enrolled in courses added by loggedin teacher
        course = Course.objects.filter(teacher=current_user)
        studentcourse=[]
        for i in course:
            sc = StudentCourse.objects.filter(course=i)
            if sc.exists():
                for j in sc:
                    studentcourse.append(j)
        print("studentcourse:",studentcourse)
        #pagination
        paginator = Paginator(studentcourse,4)
        page = request.GET.get('page', 1)
        try:
            studentcourse = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'StudentDetails.html', {'studentcourse':studentcourse, 'sub':sub, 'getid':getid})
        
def AddMarks(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        sub_id=request.POST.get('sub_id','')
        submission_marks=request.POST.get('submission_marks','')
        s=Submission.objects.get(submission_id=sub_id)
        s.submission_marks=submission_marks
        s.save()
        assign_id=request.POST.get('assign_id','')
        print(assign_id)
        assignment=Assignment.objects.get(assignment_id=assign_id)
        sc = Submission.objects.filter(submission_assignment=assignment)
        print(sc)
        sc1 = []
        for i in sc:
            sc1.append(i)
        print(sc1)
        return render(request,'ViewAssignmentSubmission.html',{'sc1':sc1, 'assign_id':assign_id})

def DeleteAssignment(request):
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        assignment=Assignment.objects.get(assignment_id=getid)
        assignment.delete()
        msg="Deleted successfully!!"
        return Home(request)