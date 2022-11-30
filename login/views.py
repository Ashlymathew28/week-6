from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
              
       username=request.POST['user']
       password=request.POST['pass']

       user= authenticate(username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('homepage')
       else:
           return render(request,'userlogin.html',{'invalid':"Invalid Credentials"})
    else:
        return render(request,'userlogin.html')
    
  
  

def  registration(request):
 # response=('registration.html')
  #return response
  print('helo')
  if request.method == 'POST':
     email=request.POST['email']
     username=request.POST['username']
     password=request.POST['password']
     confirm=request.POST.get('confirm',False)

     if password == confirm:
        if User.objects.filter(username=username).exists():
             
             return render(request,'registration.html',{'error_msg':"username already taken"})
        else: 
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            print('user created')
            return redirect('homepage')
     else:
         print("wrong password")
         return render(request,'registration.html',{'pass_msg':"wrong password"})

  else:
      print('ashly')
      return render(request,'registration.html')

def homepage(request):
    if request.user.is_authenticated:
       return render(request,'homepage.html')
    return redirect(userlogin)

def userlogout(request):
    if request.user.is_authenticated:
       logout(request)
       return redirect('userlogin')

