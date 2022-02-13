from unicodedata import name
from django.urls import path
from . import views
app_name='regist'
urlpatterns=[
    path('',views.regist,name='regist'),
    path('getregist/',views.getregist,name='getregist')
]