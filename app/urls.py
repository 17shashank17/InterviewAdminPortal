from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from django.urls import re_path as url

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'interviews', views.InterviewSet)
router.register(r'interviewer', views.InterviewerListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^addParticipants', views.addParticipants),
    url(r'^addInterviewer', views.addInterviewer),
    url(r'^checkSlot', views.checkIfSlotAvailableForParticipant),
]
