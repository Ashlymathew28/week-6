from django.forms import PasswordInput
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import user_form
from django.contrib.auth import authenticate,login,logout
from django.template import context



# Create your views here.



def adminlogin(request):
    if request.user.is_superuser:
       return redirect('adminpage')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('adminpage')
            else:
                  return render(request,'admin login.html',{'invalid':"Invalid Credentials"})
    else:
         return render(request,'admin login.html')

def adminpage(request):
    new=User.objects.all()
    context = {'user_list':new}
    return render(request,'adminpage.html',context)

def admin_logout(request):
    return redirect('adminlogin')



#@login_required(login_url='adminlogin')
def user_insert(request,id):

    user=User.objects.get(id=id)
    form=user_form(instance=user)
    if request.method == 'POST' :
        form=user_form(request.POST, instance=user)
        print('>>>>>>>>>>>>>>')
        if form.is_valid():
           print('}}}}}}}}}}}}}}}}}}}}}}')
           form.save()
           return redirect('adminpage')

    return render(request,'admin_creation.html',{'form':form})

def admin_delete(request,id):
     User.objects.get(id=id).delete()
     return redirect('adminpage')

def add_user(request):
    print('helo')
    if request.method == 'POST':
       email=request.POST['email']
       username=request.POST['username']
       password=request.POST['password']
      
      # if password == confirm:
       if User.objects.filter(username=username).exists():
             
             return render(request,'adduser.html',{'error_msg':"username already taken"})
       else: 
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('user created')
            return redirect('adminpage')
      # else:
           #print("wrong password")
           #return render(request,'adduser.html',{'pass_msg':"wrong password"})
    else:
       print('ashly')
       return render(request,'adduser.html')


    #return render(request,'adduser.html')

def search(request):
    
    if request.method=='GET':
        print("search")
        query=request.GET.get('query')
        if query:
           print("admin")
           user=User.objects.filter(username__icontains=query)
           context={'user_list':user}
           return render(request,'adminsearch.html',context)
        

        else:
            print("no data")
            return render(request,'adminpage.html')