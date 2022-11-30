from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import context
# Create your views here.



def adminlogin(request):
    context = {'user_list': User.objects.all()}
    return render(request,'admin login.html',context)

def adminpage(request):
    return render(request,'userlist.html')
