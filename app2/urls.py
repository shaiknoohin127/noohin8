from django.urls import path
from app2.views import *
app_name='app_2'
urlpatterns=[
     path('app_fun1/',app_fun1,name='app_fun1'),
 ]