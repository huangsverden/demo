from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from LoginTest.models import User

u=0
def login(requst):
    c={}
    c.update(csrf(requst))
    return render_to_response("login.html",c)

def auth_view(requst):
    username=requst.POST["username"]
    password=requst.POST["password"]
    #user=auth.authenticate(username=username,password=password)
    global u
    u=User.objects.filter(username = username,password= password)

    if u:
        #auth.login(requst,user)
        return HttpResponseRedirect("/accounts/loggedin/")
    else:
        return HttpResponseRedirect("/accounts/invalid/")

def loggedin(request):
    print(u)
    return render_to_response("loggedin.html",
                              {"full_name":u[0].username})

def invalid_login(request):
    return render_to_response("invalid_login.html")

def logout(request):
    auth.logout(request)
    return render_to_response("logout.html")

def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    args={}
    args.update(csrf(request))
    args["form"]=UserCreationForm()
    return render_to_response("register.html",args)

def register_success(request):
    return render_to_response('register_success.html')