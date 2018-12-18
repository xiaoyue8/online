# Create your views here.
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response


class UserForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

def login(req):
	if req.method == "POST":
		uf = UserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			print username,password
			return HttpResponse('login ok')
	else :
		uf = UserForm()
	return render_to_response('login.html',{'uf':uf})