from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from courses.models import Course
from courses.forms import ContactCourse

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

    contexto = {}

    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            
            form.send_mail(course)

            contexto['is_valid']=True
            print(form.cleaned_data) 
            form = ContactCourse()
    else:
        form = ContactCourse()

    contexto['form']=form
    contexto['course']=course

    return render(request,'details.html',contexto)