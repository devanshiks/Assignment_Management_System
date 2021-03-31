from django.conf.urls import url
from django.urls import path
from login.views import StudentRegister,TeacherRegister,Select,Login,TeacherRegisterPage,StudentRegisterPage,LoginPage,Logout

urlpatterns = [
    path('', LoginPage),
    url(r'^StudentRegisterPage/',StudentRegisterPage),
    url(r'^TeacherRegisterPage/',TeacherRegisterPage),    
    url(r'^StudentRegister/',StudentRegister),
    url(r'^TeacherRegister/',TeacherRegister),
    url(r'^Login/',Login),
    url(r'^Select/',Select),
    url(r'Logout/',Logout),

]
