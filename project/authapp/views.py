from django.shortcuts import redirect, render

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password ≠ get_confirm_password:
            messages.info(request, "Password is not macthing")
            return redirect('/auth/singup')
        try:
            if user.objects.get(username=get_email):
                messages.warning(request, "Email is taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request)

    
        
    return render(request, 'signup.html')  

def handleLogin(request):
    return render(request, 'login.html')

def handleLogout(request):
    return render(request, 'login.html')