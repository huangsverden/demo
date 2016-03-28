from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
from django import forms

# Create your views here.
class UserForm(forms.Form):
    name=forms.CharField()


def index(req):
    if req.method=='POST':
        form=UserForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("ok")
    else:
        form=UserForm()
    return render_to_response("register.html",{'form':form})
