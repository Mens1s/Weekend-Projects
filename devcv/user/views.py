from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']
        print(name)
    return render(request, 'login.html')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            return render(request, 'register.html',{
                'error':'Username is already using!'
            })
        elif User.objects.filter(email=email):
            return render(request, 'register.html',{
                'error':'E-mail is already using!'
            })

        else:
            user = User.objects.create(email=email, username=username, first_name =name, last_name=surname, password = password)
            user.save()
            authenticate(request, username=username, password=password)
            
            return render(request,'index')
    return render(request, 'register.html')