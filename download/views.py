import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import File
import os
import zipfile
# Create your views here.

def index(request):
    return render(request,'download/index.html')

def download(request):
    print(request.POST)
    file_list = File.objects.all()
    file_num = File.objects.count()
    context = {
        'file_list':file_list,
        'file_num':file_num,
    }
    return render(request,'download/download.html',context)

def getfile(request,pk):
    filee = File.objects.get(id=pk)
    dirlist = os.listdir('./download/files')
    for file in dirlist:
        if file == filee.filename:
            filee.download_num += 1
            filee.save()
            if file.split('.')[1] == 'zip':
                f = zipfile.ZipFile('./download/files/'+file)
                response = HttpResponse(f)
                response['Content_Type']='multipart/form-data'
                response['Content-Disposition']='attachment;filename="'+file+'"'
                return response
            f = open('./download/files/'+file)
            response = HttpResponse(f)
            response['Content_Type']='application/octet-stream'
            response['Content-Disposition']='attachment;filename="'+file+'"'
            return response
    return HttpResponse("没有此文件")






