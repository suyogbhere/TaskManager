from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from taskapp.forms import SignupForm, LoginForm,TaskForm
from taskapp.models import Task 
# Create your views here.

def Home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            tl = form.cleaned_data['title']
            de = form.cleaned_data['description']
            dd = form.cleaned_data['due_date']
            data = Task(title=tl, description=de,due_date=dd)
            data.save()
            messages.success(request,'Task created successfully!! ')

    else:
        form = TaskForm()
    return render(request, 'home.html',{'form':form})

#signup
def User_Signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            print(un)
            messages.success(request,'Account created successfully!! ')
            form.save()
    else:
        form=SignupForm()
    return render(request,'signup.html',{"form":form})

#login
def Login(request):
        if request.method =="POST":
            form=LoginForm(request.POST,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username'] 
                upass=form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully !!')
                    return HttpResponseRedirect("/")
        else:
            form=LoginForm()
        return render(request,'login.html',{'form':form})


#logout
def User_logout(request):
    logout(request)
    messages.success(request,'logout in successfully !!')
    return HttpResponseRedirect("/login/")