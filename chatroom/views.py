import json
from turtle import left
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
from .models import Message
# Create your views here.
def chatroom(request):
    statu=request.session.get('statu')
    if(statu):
        userobj = User.objects.get(username=request.session.get('account'))
        context={'userfullname':userobj.get_full_name(),'useraccount':userobj.username}
        return render(request,'chatroom/chatroom.html',context)
    return redirect('/login')

def getinfor(request):
    value=request.GET['value']
    if(value=='allinfor'):
        enable_msg_num = request.GET['enable_msg_num']
        userobj = User.objects.get(username=request.session.get('account'))
        userobj.last_login=datetime.datetime.now()
        userobj.save()
        users = User.objects.all().exclude(username=request.session.get('account'))
        fives = datetime.timedelta(seconds=2.5)
        nowtime = datetime.datetime.now()
        usersobj={}
        if users:
            for i in users:
                if(nowtime-i.last_login<fives):
                    usersobj[i.get_full_name()]=''
        right = Message.objects.all().count()
        left = right-int(enable_msg_num)
        if(left<=0):
            msgs = Message.objects.all()
        else:
            msgs = Message.objects.all()[left:right+1]
        msgsobj={}
        num=0
        for i in msgs:
            msgsobj[num]=i.user.get_full_name()+':'+i.message
            num+=1
        context={'usersobj':usersobj,'msgsobj':msgsobj,'msgsnum':Message.objects.all().count()}
        return HttpResponse(json.dumps(context))
    elif(value=='msgcount'):
        userobj=User.objects.get(username=request.session.get('account'))
        msgs = Message.objects.filter(user=userobj)
        msgcount = 0
        for i in msgs:
            msgcount+=1
        return HttpResponse(json.dumps({'statu':'true','msgcount':str(msgcount)}))

def logout(request):
    if(request.GET['flag']=='true'):
        statu=request.session.get('statu')
        if(statu):
            context={'statu':'true'}
            response=HttpResponse(json.dumps(context))
            response.delete_cookie('sessionid')
            del request.session['statu']
            return response
        else:
            return redirect('/login/')
    else:
        return redirect('/chatroom/')

def sendmsg(request):
    userobj = User.objects.get(username=request.session.get('account'))
    Message.objects.create(user=userobj,message=request.GET['msg'])
    return HttpResponse(json.dumps({'statu':'true'}))