from django import forms
from .models import CommitteeMembers, CustomUser
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate

class CustomUserCreationFormEmail(UserCreationForm):
     class Meta:
          model = CustomUser
          fields = ['username', 'email', 'password1', 'password2']
          widgets = {
               'username': forms.TextInput(
                    attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
               ),
               'email': forms.EmailInput(
                    attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
               ),
               'password1': forms.PasswordInput(
                    attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
               ),
               'password2': forms.PasswordInput(
                    attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
               ),
          }

class CustomUserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email':forms.EmailInput(
                attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
            ),
            'password':forms.PasswordInput(
                attrs={'class': 'p-2 text-gray-700 bg-white rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
            
            )
        }
   

    


class CommitteeMembersForm(forms.ModelForm):
    class Meta:
        model = CommitteeMembers
        fields = ['member_name', 'position', 'description', 'image']
        widgets = {
            'description': forms.Textarea(
                attrs={'rows':1,'cols':40, 'class': ' inline rounded w-28   my-4 text-gray-600 p-2 outline outline-offset-2 outline-1 focus:outline-none focus:ring focus:ring-blue-400', 'placeholder': '£'}
            ) ,
        }