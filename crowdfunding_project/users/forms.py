from django import forms
from .models import User
import re


class UserForm (forms.ModelForm):
    class Meta:
        model =User
        fields=("First_name","Last_name","Email","password", "confirm_password","mobile_phone","profile_image")
    

    

