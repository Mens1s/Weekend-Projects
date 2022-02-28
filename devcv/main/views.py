from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Userdata

@login_required(login_url = 'login')
def index(request):
    return render(request, 'index.html',{
        "bio":"more than moremore than moremore than moremore than moremore than moremore than moremore than moremore than moremore than moremore than moremore than moremore than moremore than more"

    })

def username(request, user):
    if User.objects.filter(username=user):
        user = Userdata.objects.get(username=user)
        print(user)
        return render(request, 'index.html',{
            'username': user.username,
            'bio': user.bio,
            'school': user.school,
            'projects':user.projects,
        })
    else:
        return render(request, '404.html')
    

def noteditable(request):
    return render(request, )

def page_not_found(request, exception=None):
    return render(request, '404.html', {})