from email.policy import default
from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login, logout
from .models import MyUser
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',{
                'error':'Email or Password is wrong',
            })
    return render(request,'login.html')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        name = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password != repassword:
            return render(request, 'register.html',{
                'error':'password does not match',
            })
        else:
            if MyUser.objects.filter(email=email).exists():
                return render(request, 'register.html', {
                    'error':'email is already using',
                })
            else:
                
               
                user= MyUser.objects.create(email=email, first_name=name, last_name=lastname,
                btcBalance=request.POST["btcBalance"],
                ethBalance=request.POST["ethBalance"],
                euroBalance=request.POST["euroBalance"],
                usdBalance=request.POST["usdBalance"],
                trBalance=request.POST["trBalance"],
                investingBalance=request.POST["investingBalance"],
                )
                realUser = User.objects.create_user(username=email, email=email, first_name=name, last_name=lastname, password=password)
                realUser.save()
                user.save()

                user = authenticate(request, username=email, password=password)
                login(request, user)

                return redirect('index')
                # return render(request, 'login.html', {
                #     'succes':'registered succesfully! you can login',
                # })
    return render(request,'register.html')
