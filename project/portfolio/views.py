from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')  

def handleservices(request):
    return render(request, 'services.html') 

def resume(request):
    return render(request, 'resume.html') 

def skills(request):
    return render(request, 'skills.html') 

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphonenumber=request.POST.get('num')
        fdescription=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request, "Thanks for contacting us.We will get to you Soon!")

        return redirect('/contact')
    
    return render(request, 'contact.html')