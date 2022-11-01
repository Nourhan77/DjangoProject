from django.shortcuts import render
from .forms import UserForm 
from .models import User
from .tokens import activation_token
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.messages import constants as messages
from django.contrib.auth import login as auth_login
from projects.models import Project
from django.contrib.auth import authenticate, login



def login_user(request):
    if request.method== "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = get_object_or_404(User,Email=email, password=password)
        if user is not None:
            return redirect("profile",user_id=user.id)
        else:
            messages.success(request,"Sorry user is not found")
            return redirect('login')
    else :
        return render (request,'user/login.html')


def activate(req, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except(TypeError, ValueError):
        user = None
    if user and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(req, 'Your Account activated. Now Login')
        return redirect("user/Register")
    else:
        messages.error(req, "Activation  link is Invalid.")





def register(request):
    # Validate the user registration data
    form = UserForm()
    if request.method=="POST":
        form=UserForm(request.POST, request.FILES)
        if form.is_valid():
           
            user=form.save() 
            user.clean_mobile(user.mobile_phone)
            return redirect ("profile",user_id=user.id)
    return render (request ,'user/Register.html' , {'form':form})

def profile (request,user_id):
    user=User.objects.get(id=user_id)
    projects=Project.objects.filter(user=user.id)
    
    print(user.profile_image.url)
    context={
        "user":user,
        "projects":projects

    }
    return render (request,"user/profile.html",context)


def editUser(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    if request.method=="POST":
        if user:
            user.First_name=request.POST.get('first')
            user.Last_name=request.POST.get('second')
            
            user.country=request.POST.get('country')
            
            user.mobile_phone=request.POST.get('mobile_phone')
            user.facebook=request.POST.get('facebook')
            user.birthdate=request.POST.get('birthdate')
            user.save()
            return redirect('profile',user_id=user.id)
    else:
        form = UserForm(instance=user)
    return render (request ,'user/update.html' , {'form':form})
