from unicodedata import name
from . import views
from django.urls import path
app_name = 'chatroom'
urlpatterns=[
    path('',views.chatroom,name='chatroom'),
    path('logout/',views.logout,name='logout'),
    path('getinfor/',views.getinfor,name='getinfor'),
    path('sendmsg/', views.sendmsg, name='sendmsg')
]