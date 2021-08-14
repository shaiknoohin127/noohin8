from django.shortcuts import render

# Create your views here.
def app_fun(request):
    return render(request,'app1/noohin.html')