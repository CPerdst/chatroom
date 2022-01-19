from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import time
import json
from login.models import User
from chatroom.models import Msg
# Create your views here.
def index(request):
    return render(request,'chatroom/index.html')
def getinfor(request):
    try:
        Check()
        userid = request.COOKIES.get('userid')
        myjs = ropen()
        myjs[userid]=str(time.time())
        wopen(json.dumps(myjs))
        usernames={}
        msgs = {}
        a=1
        for i in myjs:
            username = User.objects.get(id=int(i)).username
            usernames[username]=''
        for i in Reverse(Msg.objects.all())[:10]:
            msgs[str(a)+':'+i.user.username]=i.msg
            a+=1
        if Msg.objects.all().count()>10:
            for n in Msg.objects.all()[:Msg.objects.all().count()-10]:
                n.delete()
        # print(msgs)
        context = {"users":usernames,"username":User.objects.get(id=int(userid)).username,"msgs":msgs}
        return HttpResponse(json.dumps(context,ensure_ascii=False))
    except:
        with open('D:/Codes/Python-Codes/lg3/chatroom/time.txt','r') as f:
            mystr = f.read()
            f.close()
        mystr = list(mystr)
        mystr.pop()
        s=''
        for i in mystr:
            s+=i
        with open('D:/Codes/Python-Codes/lg3/chatroom/time.txt','w') as f:
            f.write(s)
        return HttpResponse('false')

def sendmsg(request):
    msg = request.GET['msg']
    userobj = User.objects.get(id=int(request.COOKIES.get('userid')))
    m = Msg.objects.create(user=userobj,msg=msg)
    m.save()
    return HttpResponse('ok')

def Check():
    myjs = ropen()
    nowt = time.time()
    name = []
    for i in myjs:
        # print(nowt-float(myjs[i]))
        if(nowt-float(myjs[i])>3):
            name.append(i)
    for i in name:
        del myjs[i]
    wopen(json.dumps(myjs))

def ropen():
    with open('D:/Codes/Python-Codes/lg3/chatroom/time.txt','r') as f:
        myjs = json.loads(f.read())
        f.close()
    return myjs

def wopen(myjsstr):
    with open('D:/Codes/Python-Codes/lg3/chatroom/time.txt','w') as f:
        f.write(myjsstr)

def Reverse(lst):
    return [ele for ele in reversed(lst)]