#from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        #model=CustomUser
        fields=('email', 'username')
        #UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        #model=CustomUser
        model = get_user_model()
        fields=('email', 'username')
        #UserCreationForm.Meta.fields
