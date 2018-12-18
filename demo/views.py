# Create your views here.
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth


class UserForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

def login(req):
	if req.method == "POST":
		uf = UserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			
			re = auth.authenticate(username=username,password=password)
			if re is not None: 
				auth.login(req,re)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/login/')
	else :
		uf = UserForm()
	return render_to_response('login.html',{'uf':uf})
	
def index(req):
	username = User.objects.get(username__exact='dd')
	return render_to_response('index.html',{'username':username})