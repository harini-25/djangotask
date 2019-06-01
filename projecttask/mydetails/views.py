from django.shortcuts import render
from django.http import HttpResponse
# from .models import Ourdetails
# import models import Ourdetails

# Create your views here.
def Welcome(request):
    # d=Ourdetails.objects.all()
    # d="hello"
    # return HttpResponse('HI WELCOME TO MYPAGE.')
    # return render(request,'Welcome.html',{'data':d})
    return render(request, 'Welcome.html', {})

def Table(request):
    return render(request,'tablee.html',{})

def Looping(request,number):
    # return HttpResponse("Hi Welcome %s." % Employees.objects.get.user_name)
    a=[]
    for i in range(0,number): 
        a.append(i)
    print(a)
    return render(request,'loopind.html',{'data':a})

    