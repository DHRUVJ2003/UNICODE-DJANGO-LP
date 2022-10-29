import imp
import re
import string
from django.urls import reverse
from xml.dom import UserDataHandler
from django import forms
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.forms import CharField, ModelForm
from .form import T,signin
from .models import USER,TD
import requests
from django.contrib.auth import authenticate ,login as loginUser,logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.decorators import login_required
# def form(request):
#     if request.method=="GET":
#         form=USE()
#         context={'form':form}
#         return render(request,'inform.html',context)
#     if request.method=="POST":
#         rm=request.POST.get('username')
#         if(USER.objects.filter(username=rm).exists()==True):
#             display= TD.objects.filter(user_id=(USER.objects.get(username=rm)).username).values()
#             # print (display)
#                 # display= TD.objects.filter(user_id=name).values()
#             ans={'display':display}
#             return render(request,'outform.html',ans)
#         else:
#             rm=USER(username=rm) 
#             rm.save()
#             ans={'display':{}}
#             return render(request,'outform.html',ans)
@login_required(login_url='login')
def main(request):
    if request.user.is_authenticated:
        user = request.user
        # form = T()
        display = TD.objects.filter(user = user).order_by('start_date_time')
        return render(request , 'outform.html' , context={'display' : display})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('main')
        else:
            context = {
                'form' : form
            }
            return render(request , 'login.html' , context=context )

def signup(request):
    if request.method=='GET':
        signform=signin()
        context={'signform':signform}
        return render (request,'sign.html',context)
    else:
        signform=signin(request.POST,request.FILES)
        if signform.is_valid==True:            
            # password=signform.cleaned_data.get('password')
            # user.set_password(password)
            user=signform.save()
            authenticate(username=user.username,password=user.password)
            return redirect('login')
        else:
            return redirect('signup')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method=="GET":
            todo=T()
            context={'todo':todo}
            return render(request,'todo.html',context)
        if request.method=="POST":
            todo=T(request.POST)
            if todo.is_valid():
                task=todo.cleaned_data['task']
                task_description=todo.cleaned_data['task_description']
                num=todo.cleaned_data['num']
                status=todo.cleaned_data['status']
                start_date_time=todo.cleaned_data['start_date_time']
                end_date_time=todo.cleaned_data['end_date_time']
                td=TD(task=task,task_description=task_description,num=num,user=user,status=status,start_date_time=start_date_time,end_date_time=end_date_time)
            td.save()
            return redirect('main')
            # display= TD.objects.filter(user_id=user_id).order_by('start_date_time').values()
            # ans={'display':display}
            # return render(request,'outform.html',ans)


@login_required(login_url='login')
def deletet(request,id):
    if request.method == 'POST':
        p=TD.objects.filter(id=id)
        p.delete()
        return redirect('main')
        # return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
        # print (p)

# def deleteu(request):
#     if request.method == 'GET':
#         p=USE()
#         context={'p':p}
#         return render(request,'userdel.html',context)
#     if request.method == 'POST':
#         w=request.POST.get('username')
#         p=USER.objects.filter(username=w)
#         # print(p)
#         p.delete()
#         return redirect('form')


@login_required(login_url='login')
def update(request,id):
    if request.method=='GET':
        pi=TD.objects.get(id=id)
        fm=T(instance=pi)
        return render(request,'update.html',{'form':fm})
    else:
        pi=TD.objects.get(id=id)
        fm=T(request.POST,instance=pi)
        if fm.is_valid:
            fm.save()
        return redirect('main')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        # form = T()
        username=user.username
        print(username)
        display = USER.objects.get(username=username)
        return render(request , 'profile.html' , context={'display' : display})

def logt(request):
    logout(request)
    return redirect('login')