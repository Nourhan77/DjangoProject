from asyncio.windows_events import NULL
from django.shortcuts import render
from .forms import UserForm
from .models import User
from .tokens import activation_token
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.messages import constants as messages
from django.contrib.auth import login as auth_login
from projects.models import Project
from projects.forms import TagForm
import re

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
    error_message=NULL
    if request.method=="POST":
        form=UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Validation on password
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            if password != confirm_password:
                error_message="Password and confirmation not matching"
            else:
                error_message="valid"

            # Validation on mobile_phone number
            mobile=request.POST.get('mobile_phone')
            if  (not re.fullmatch("01[0125][0-9]{8}",mobile)):
                error_message="Invalid mobile phone number it should be like that 01123456789"
            else:
                error_message="valid"



            if error_message=="valid":
                user=form.save() 
                return redirect ("profile",user_id=user.id)
            
    return render (request ,'user/Register.html' , {"error":error_message,'form':form})




def profile (request,user_id):
    user=User.objects.get(id=user_id)
    projects=Project.objects.filter(user=user.id)

    context={
        "user":user,
        "projects":projects

    }
    return render (request,"user/profile.html",context)


def editUser(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    form = UserForm(instance=user)

    error_message=NULL
    if request.method=="POST":
        if user:
            user.First_name=request.POST.get('First_name')
            user.Last_name=request.POST.get('Last_name')
            user.country=request.POST.get('country')
            user.mobile_phone=request.POST.get('mobile_phone')
            user.facebook=request.POST.get('facebook')
            user.birthdate=request.POST.get('birthdate')
            if  (not user.First_name or not user.Last_name or not user.mobile_phone ):
                error_message="Complete Info"
            else:
                error_message="valid"
            
            if error_message=="valid":
                user.save() 
                return redirect ("profile",user_id=user.id)
    
    print(user.id)
    return render (request ,'user/update.html' , {"user":user  ,"error":error_message,'form':form})


def CreateTag (request,user_id):
    
    if request.method=="POST":
        form=TagForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect ("profile",user_id=user_id)
    
    else:
        form = TagForm()
    return render (request ,'user/tags.html' , {"user_id":user_id,'form':form})
