from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from .models import Users

# User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hey {username}, You account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request,new_user)
            return redirect("core:home")
            
    else:
        form = UserRegisterForm()

    context = {
        'form':form,
    }

    return render(request,'userauths/register.html',context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,"Hey you are already logged in")
        return redirect("core:home")
    
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(email=email)
            user = authenticate(request, email=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in.")
                return redirect("core:home")
            else:
                messages.warning(request,"User Does Not Exits, create an account")
    
        except:
            messages.warning(request,f"User with {email} does not exits")
        
        
    return render(request,"userauths/login.html")



def logout_view(request):
    logout(request)
    messages.success(request,"You logged out")
    return render(request,'core/index.html')

        