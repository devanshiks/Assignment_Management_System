from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from login.models import Student, Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def StudentRegisterPage(request):
    return render(request, 'StudentRegister.html', context=None)

def TeacherRegisterPage(request):
    return render(request, 'TeacherRegister.html', context=None)

def LoginPage(request):
    c = {} 
    c.update(csrf(request))
    return render(request, 'Login.html', context=None)

def Logout(request):
    auth.logout(request)
    return redirect('/')

def StudentRegister(request):
    stu_email=request.POST.get('stu_email','')
    stu_name=request.POST.get('stu_name','')
    stu_branch=request.POST.get('stu_branch','')
    stu_gender=request.POST.get('stu_gender','')
    stu_sem=request.POST.get('stu_sem','')
    stu_dob=request.POST.get('stu_dob','')
    stu_address=request.POST.get('stu_address','')
    stu_city=request.POST.get('stu_city','')
    stu_state=request.POST.get('stu_state','')
    stu_zip=request.POST.get('stu_zip','')
    stu_mobile_no=request.POST.get('stu_mobile_no','')
    password=request.POST.get('stu_password','')
    repassword=request.POST.get('stu_repassword','')
    stu = Student.objects.filter(stu_email=stu_email)
    if password!=repassword or len(password)<6:
        msg_pass="password and confirm password must be same with minimum length 6"
    else:
        msg_pass=''
    if len(stu_mobile_no)!=10:
        msg_phone="phone number must be of length 10, please fill the form again with correct contact no"
    else:
        msg_phone=''
    if len(stu_zip)!=6:
        msg_zip="zip code must be of corrct length of 6 , please fill the form again with correct contact no"
    else:
        msg_zip=''
    if stu.exists() :
        msg_email = "This email is already registered"
    else:
        msg_email = ''
    if not ( msg_phone or msg_zip or msg_email or msg_pass):
        user=User.objects.create_user(username=stu_email,email=stu_email,password=password)
        user.save()
        stu=Student(stu_name=stu_name,stu_email=stu_email,stu_gender=stu_gender,stu_sem=stu_sem,stu_city=stu_city,
        stu_branch=stu_branch,stu_dob=stu_dob,stu_address=stu_address,stu_state=stu_state,stu_zip=stu_zip,stu_mobile_no=stu_mobile_no)
        stu.save()
        msg="You are registered!"
        return render(request ,'Login.html',{'msg':msg})
    else:
        return render(request ,'StudentRegister.html',{'msg_phone':msg_phone, 'msg_email':msg_email, 'msg_zip':msg_zip, 'msg_pass':msg_pass})

def TeacherRegister(request):
    teach_email=request.POST.get('teach_email','')
    teach_name=request.POST.get('teach_name','')
    teach_gender=request.POST.get('teach_gender','')
    teach_dob=request.POST.get('teach_dob','')
    teach_address=request.POST.get('teach_address','')
    teach_city=request.POST.get('teach_city','')
    teach_state=request.POST.get('teach_state','')
    teach_zip=request.POST.get('teach_zip','')
    teach_mobile_no=request.POST.get('teach_mobile_no','')
    password=request.POST.get('teach_password','')
    repassword=request.POST.get('teach_repassword','')
    t = Teacher.objects.filter(teach_email=teach_email)
    if password!=repassword or len(password)<6:
        msg_pass="password and confirm password must be same with minimum length 6"
    else:
        msg_pass=''
    if len(teach_mobile_no)!=10:
        msg_phone="phone number must be of length 10, please fill the form again with correct contact no"
    else:
        msg_phone=''
    if len(teach_zip)!=6:
        msg_zip="zip code must be of corrct length of 6 , please fill the form again with correct contact no"
    else:
        msg_zip=''
    if t.exists() :
        msg_email = "This email is already registered"
    else:
        msg_email = ''
    if not ( msg_phone or msg_zip or msg_email or msg_pass):
        user=User.objects.create_user(username=teach_email,email=teach_email,password=password)
        user.save()
        teach=Teacher(teach_name=teach_name,teach_email=teach_email,teach_gender=teach_gender,teach_city=teach_city,
        teach_dob=teach_dob,teach_address=teach_address,teach_state=teach_state,teach_zip=teach_zip,teach_mobile_no=teach_mobile_no)
        teach.save()
        msg="You are registered!"
        return render(request ,'Login.html',{'msg':msg})
    else:
        return render(request ,'TeacherRegister.html',{'msg_phone':msg_phone, 'msg_email':msg_email, 'msg_zip':msg_zip, 'msg_pass':msg_pass})

def Select(request):
    return render(request, 'Select.html')

def Login(request):
    email = request.POST.get('email', '')
    password=request.POST.get('password','')
    User=auth.authenticate(username=email,password=password)
    teach = Teacher.objects.filter(teach_email=email)
    stu = Student.objects.filter(stu_email=email)
    if teach.exists():
        auth.login(request,User)
        return HttpResponseRedirect('/Teacher/Home/')
    elif stu.exists():
        auth.login(request,User)
        return HttpResponseRedirect('/Student/StudentHomePage/')
    else:
        msg = "Invalid Username or Password!"
        return render(request,'Login.html', {'msg':msg})