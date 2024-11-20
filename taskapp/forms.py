from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from taskapp.models import Task


class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={"class":"form-control"}))
                
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        labels={"first_name":"First Name","last_name":"Last Name","email":"Email"}
        widgets={"username":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),}

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","autofocus":True}))


#custom date widget
class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','due_date']    
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':"3",'cols':"12"}),
            'due_date':DateTimeInput(attrs={'class':'form-control'})
        }