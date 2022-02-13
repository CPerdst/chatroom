from datetime import date, datetime
from tkinter.tix import Tree
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json,random

from django.template import context
# Create your views here.
def login(request):
    statu=request.session.get('statu')
    if(statu):
        return redirect('/chatroom/')
    else:
        return render(request,'login/login.html')

def checklogin(request):
    user = User.objects.filter(username=request.GET['account'])
    if user:
        if(user[0].password==request.GET['password']):
            request.session['statu']=True
            request.session['account']=request.GET['account']
            mydict={
                'statu':'true','information':'登录成功!'
            }
            return HttpResponse(json.dumps(mydict))
        else:
            mydict={
                'statu':'false','information':'账号密码不匹配!'
            }
            return HttpResponse(json.dumps(mydict))
    else:
        mydict={
                'statu':'false','information':'没有此账号!'
            }
        return HttpResponse(json.dumps(mydict))

def regist(request):
    return render(request,'regist/regist.html')

def getregist(request):
    first_name = request.GET['first_name']
    last_name = request.GET['last_name']
    password = request.GET['password']
    email = request.GET['email']
    user = User.objects.filter(email=email)
    if user:
        mydict={'statu':'false','information':'已有此邮件用户,请确认您的邮件是否正确!,或者尝试<a href="/login/">点此</a>登录'}
        return HttpResponse(json.dumps(mydict))
    else:
        account = random.randint(10000000,99999999)
        User.objects.create(first_name=first_name,last_name=last_name,password=password,username=account,email=email,last_login=datetime.now())
        mydict={'statu':'true','information':'注册成功,您的账号为'+str(account)+',<a href="/login">点此</a>登录'}
        return HttpResponse(json.dumps(mydict))

def forgetaccount(request):
    try:
        email = request.GET['email']
    except:
        return render(request,'login/forgetaccount.html')
    
    if email:
        users = User.objects.filter(email=email)
        if users:
            context={'statu':'true','information':{'account':users[0].username,'username':users[0].get_full_name()}}
            return HttpResponse(json.dumps(context))
        else:
            context={'statu':'false','information':'未找到拥有此邮箱的用户,请检查输入是否正确!'}
            return HttpResponse(json.dumps(context))
        