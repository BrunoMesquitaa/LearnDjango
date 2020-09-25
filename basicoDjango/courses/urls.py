from django.contrib import admin
from django.urls import path
from courses.views import courses


app_name='curso'
urlpatterns = [
    path('',courses, name="curso")
]