from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            print("gir")
            login(request, user)
            return redirect("index")
        else:
            print("girme")
            render(request, 'login.html', {
                'error':'Password or/and Username is wrong!',
            })

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
            user = User.objects.create_user(email=email, username=username, first_name =name, last_name=surname, password = password)
            user.save()
            authenticate(request, username=username, password=password)
            
            return render(request,'index.html')
    return render(request, 'register.html')