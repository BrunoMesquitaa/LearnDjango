from django.shortcuts import render
from django.http import HttpRequest
from courses.models import Course

# Create your views here.
def courses(request):
    contexto={
        'courses':Course.objects.all()
    }
    return render(request,'courses.html', contexto)