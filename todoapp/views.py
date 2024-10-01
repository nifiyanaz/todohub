from django.shortcuts import  redirect, render
from .models import Tasks
from .form import SignupForm, TaskForm,LoginForm
from django.contrib.auth import authenticate




def index(request):
    tasks=Tasks.objects.all()
    return render(request,'home.html',{'task':tasks})

def addtask(request):
    
    form=TaskForm()
    if request.method=='POST':
       form=TaskForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('displya')
       else:
           form=TaskForm()
    else:
        form=TaskForm()
        return render(request,'addtask.html',{'form':form})
    
def displya(request):
    tasks=Tasks.objects.all()
    return render(request,'displya.html',{'tasks':tasks})

def user_login(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                user_login(request,user)
                return redirect ('home')
        # else:
        #     form=LoginForm()
           
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    return render(request,'logout.html')
    
def user_signup(request):
    if request.POST:
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form}) 


def delete_task(request,task_id):
   
   task=Tasks.objects.get(id=task_id)
   task.delete()
   return redirect('displya')