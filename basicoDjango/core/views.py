from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{"usuario":"NETTO"})

def base(request):
    return render(request,'base.html')

def contato(request):
    return render(request,'contact.html')