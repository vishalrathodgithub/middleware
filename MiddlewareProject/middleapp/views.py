from django.shortcuts import render,HttpResponse
from middleapp.forms import LoginForm
from django.db.module.signals import Signal

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello HttpResponse........</h1>")
def home_view(request):
    form=LoginForm()
    return render(request,"middleapp/home.html",{"form":form})
def home2(request):
    form=LoginForm()
    name1=request.POST.get("username")
    request.session["username1"]=name1
    return render(request,"middleapp/home1.html",{"form":form})
def home3(request):
    form=LoginForm()
    name2=request.POST.get("username")
    request.session["username2"]=name2
    return render(request,"middleapp/home2.html",{"form":form})
def home4(request):
    name3=request.POST.get("username")
    request.session["username3"]=name3
    return render(request,"middleapp/home3.html")
