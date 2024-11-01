from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')  

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('num')
        desc=request.POST.get('desc')
        messages.info(request, f'the name is {name} ,email is {email} ,your number is {phonenumber} adn your query is {desc}')

        return redirect('/contact')
    
    return render(request, 'contact.html')