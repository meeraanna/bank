from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import appform


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)

        # if user is not None:
        #     # auth.login(request,user)
        #     return redirect('/bankapp/login/newpage')
        # else:
        #     messages.info(request,'Invalid')
        #     return redirect('/bankapp/login/')
        return redirect('/bankapp/login/newpage')
    return render(request,'login.html')

def newpage(request):
    return render(request,'newpage.html')


def Register(request):
    if request.method == 'POST':
            username = request.POST['username']
            password= request.POST['password']
            cpassword = request.POST['cpassword']

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist')
                    return redirect('/bankapp/login/register/')
                else:
                    user=User.objects.create_user(username=username,password=password)
                    user.save()
                    return redirect('/bankapp/login')
            else:
                messages.info(request,'Incorrect password')
                return redirect('/bankapp/login/register/')
    return render(request,'register.html.')

def appform(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        dob=request.POST.get('dob')
        age=request.POST.get('age','')
        address= request.POST.get('address','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        gender=request.POST.get('gender')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        accountype=request.POST.get('accountype')
        material=request.POST.get('material1')


        meera=appform(name=name,age=age,dob=dob,address=address,email=email,phone=phone,
                      gender=gender,account=accountype,material=material,
                      district=district,branch=branch)


        meera.save()
    # messages.success(request, 'application accepted')

    return render(request,'appform.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






