from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    # print(request.GET)
    try:
        account = request.GET['account']
        password = request.GET['password']
        userobj = User.objects.filter(account=account,password=password)
        # print(userobj[0].id)
        if(userobj):
            response = HttpResponse('login successfully')
            response.set_cookie('userid',userobj[0].id,expires=60*60*24)
            return response
        else:
            response = HttpResponse('账号或密码错误')
            response.delete_cookie('userid')
            return response
    except:
        return render(request,'login/index.html')

def regist(request):
    print(request.GET)
    try:
        username=request.GET['username']
        account=request.GET['account']
        password=request.GET['password']
        userobj = User.objects.filter(account=account)
        if(userobj):
            json = '{"state":"0","information":"此账号已被注册!"}'
            print(str(json))
            return HttpResponse(json)
        else:
            user = User.objects.create(username=username,account=account,password=password)
            user.save()
            json = '{"state":"1","information":"注册成功<a href=\'/login/\'>点我<a/>登录"}'
            print(str(json))
            response = HttpResponse(json)
            response.set_cookie('userid',user.id,expires=60*60*24)
            return response
    except:
        return render(request,'login/regist.html')

def reurl(request):
    return render(request,'login/reurl.html')