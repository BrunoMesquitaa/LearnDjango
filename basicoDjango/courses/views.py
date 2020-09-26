from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from courses.models import Course

# Create your views here.
def courses(request):
    contexto={
        'courses':Course.objects.all()
    }
    return render(request,'courses.html', contexto)

# def detalhes(request,pk):
#     course = get_object_or_404(Course,pk=pk)
#     return render(request,'details.html',{"course":course})

def detalhes(request,title):
    course = get_object_or_404(Course,slug=title)
    return render(request,'details.html',{"course":course})