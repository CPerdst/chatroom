from unicodedata import name
from django.urls import path
from . import views
app_name = 'chatroom'
urlpatterns=[
    path('',views.index,name='chatroom'),
    path('getinfor/',views.getinfor,name='getinfor'),
    path('sendmsg/',views.sendmsg,name='sendmsg')
]