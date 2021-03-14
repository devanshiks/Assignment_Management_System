from django.conf.urls import url
from teacher.views import Home

urlpatterns = [
    url(r'^Home/',Home),
]