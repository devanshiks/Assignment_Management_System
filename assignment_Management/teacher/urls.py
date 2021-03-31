from django.conf.urls import url
from teacher.views import Home, CoursesPage,AddCourse,AddAssignment,StudentDetailsPage,ViewAssignmentSubmission,AddMarks,ViewStudentSubmission
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^Home/',Home),
    url(r'^CoursesPage/',CoursesPage),
    url(r'^AddCourse/',AddCourse),
    url(r'^AddAssignment/',AddAssignment),
    url(r'StudentDetailsPage/',StudentDetailsPage),
    url(r'ViewAssignmentSubmission/',ViewAssignmentSubmission),
    url(r'AddMarks/',AddMarks),
    url(r'ViewStudentSubmission/',ViewStudentSubmission)

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
