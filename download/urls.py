import imp
from django.urls import path
from . import views
app_name = 'download'

urlpatterns = [
    path('',views.index,name='index'),
    path('Download/',views.download,name='download'),
    path('Download/<int:pk>/',views.getfile,name='getfile'),
]