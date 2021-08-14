from django.urls import path
from app1.views import *
app_name='app_1'
urlpatterns=[
     path('app_fun/',app_fun,name='app_fun'),
 ]