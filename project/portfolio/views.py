from django.shortcuts import render, redirect

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
        print(name,email,phonenumber,desc)
        return redirect('/contact')
    
    return render(request, 'contact.html')