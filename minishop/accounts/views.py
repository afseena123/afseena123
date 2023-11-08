from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def loadlogin(request): 
    if request.method=="POST":
        un=request.POST["username"]
        pwd=request.POST["password"]
        # print(un)
        # print(pwd)
        # fetching
        user=auth.authenticate(username=un,password=pwd)
        print(user)
        if user is not None:
            # print("hai")
            auth.login(request,user)
            return redirect('/')
        else:
           
            messages.info(request,'Data is Invalid!!!!!')
            return redirect('loadlogin')
    else:           
        return render(request,'login.html')


def loadregister(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['email']
        un=request.POST['username']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']
        if pwd==cpwd:
            if User.objects.filter(username=un).exists():
             
                messages.info(request,"Username Already taken!!!!")
             
                return redirect("loadregister")
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"This email is already taken!!!")
                 return redirect("loadregister")
            else:
                # insertion code 
                reg=User.objects.create_user(first_name=fn, last_name=ln,email=email, username=un, password=pwd)
                reg.save()
                print("User created successfullty...")
        else:
          #   messages.info(request,"Password is not match!!!")
            print("Password is not match!!!")
            return redirect("loadregister")
        return redirect("/")
    else:

        return render(request,'register.html')
    

def loadlogout(request):
    auth.logout(request)
    return redirect('/')
