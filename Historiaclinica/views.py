from django.shortcuts import render,redirect
from .form import loginForm
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
	form = loginForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		username= data.get("username")
		password = data.get("password")
		acceso = authenticate(username = username,password = password)
		if acceso is not None:
			login(request,acceso)
			print (username)
			return HttpResponse("Bienvenido {}".format(username))
		else:
			return HttpResponse("Usuario / contrasena incorrectos")
	else:
		form = loginForm()

	return render(request, 'login.html',{'formulario':loginForm})