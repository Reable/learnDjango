from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

def index(req):

    features = Feature.objects.all()

    return render(req, 'index.html', {
        'features': features
    })

def counter(req):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(req, 'counter.html', {'posts': posts})

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            print(user)
            return redirect('/')
        else:
            messages.info(req, 'Invalid')
            return redirect('login')
    else:
        return render(req, 'login.html')

def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(req, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(req, 'This username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(req, 'Password not the same')
            return redirect('register')
    else:
        return render(req, 'register.html')

def logout(req):
    auth.logout(req)
    return redirect('/')

def post(req, pk):
    return render(req, 'post.html', {'pk': pk})
