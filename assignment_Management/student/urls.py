from django.conf.urls import url
from student.views import StudentHomePage,StudentCourseList,AddStudentCourse,AddSubmissionPage,AddSubmission,RemoveStudentCourse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^StudentHomePage/',StudentHomePage),
    url(r'StudentCourseList/',StudentCourseList),
    url(r'AddStudentCourse/',AddStudentCourse),
    url(r'AddSubmissionPage/',AddSubmissionPage),
    url(r'AddSubmission/',AddSubmission),
    url(r'RemoveStudentCourse/',RemoveStudentCourse),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
