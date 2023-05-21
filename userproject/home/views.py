from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Password for Admin is akshit , 1234
# Password for Admin is akshu , akshu00000
# Create your views here.
def index(request):
    #to check AnonymousUser
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        #Checkif user has entered Correct Credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
