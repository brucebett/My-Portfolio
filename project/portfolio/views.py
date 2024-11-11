from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship


# Create your views here.
def home(request):
    return render(request, 'home.html')  

def handleservices(request):
    return render(request, 'services.html') 

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect("/auth/login/")
    
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')    
        fusn=request.POST.get('usn')    
        fcolege=request.POST.get('cname')    
        foffer=request.POST.get('offer')    
        fstartdate=request.POST.get('sartdate')    
        fenddate=request.POST.get('enddate')    
        fprojreport=request.POST.get('projreport')  

# conecting to uppercase
        fname=fname.upper()  
        fusn=fusn.upper()  
        fcolege=fcolege.upper()  
        foffer=foffer.upper()  
        fprojreport=fprojreport.upper()  

        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcolege,offer_status=foffer,
                         start_date=fstartdate,end_date=fenddate,project_report=fprojreport)
        query.save()
        messages.success(request, "Form is Submitted Successfuly!")
        return redirect('/internshipdetails')

    return render(request, 'internship.html') 

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request, 'blog.html',context)

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