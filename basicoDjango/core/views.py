from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{"usuario":"BRUNO"})

def base(request):
    return render(request,'base.html')

def contato(request):
    return render(request,'contact.html')