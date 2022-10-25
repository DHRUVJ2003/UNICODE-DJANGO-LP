import imp
import string
from django.urls import reverse
from xml.dom import UserDataHandler
from django import forms
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.forms import CharField, ModelForm
from .form import USE,T
from .models import USER,TD
import requests
def form(request):
    if request.method=="GET":
        form=USE()
        context={'form':form}
        return render(request,'inform.html',context)
    if request.method=="POST":
        rm=request.POST.get('username')
        if(USER.objects.filter(username=rm).exists()==True):
            display= TD.objects.filter(user_id=(USER.objects.get(username=rm)).username).values()
            # print (display)
                # display= TD.objects.filter(user_id=name).values()
            ans={'display':display}
            return render(request,'outform.html',ans)
        else:
            rm=USER(username=rm) 
            rm.save()
            ans={'display':{}}
            return render(request,'outform.html',ans)

def add(request):
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
            user_id=todo.cleaned_data['user_id']
            start_date_time=todo.cleaned_data['start_date_time']
            end_date_time=todo.cleaned_data['end_date_time']
            td=TD(task=task,task_description=task_description,num=num,user_id=user_id,status=status,start_date_time=start_date_time,end_date_time=end_date_time)
        td.save()
        display= TD.objects.filter(user_id=user_id).order_by('start_date_time').values()
        ans={'display':display}
        return render(request,'outform.html',ans)

def deletet(request,id):
    if request.method == 'POST':
        p=TD.objects.filter(id=id)
        p.delete()
        return HttpResponseRedirect('/')
        # return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
        # print (p)

def deleteu(request):
    if request.method == 'GET':
        p=USE()
        context={'p':p}
        return render(request,'userdel.html',context)
    if request.method == 'POST':
        w=request.POST.get('username')
        p=USER.objects.filter(username=w)
        # print(p)
        p.delete()
        return redirect('form')

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
        return HttpResponseRedirect('/')