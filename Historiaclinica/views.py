from django.shortcuts import render,redirect
from .form import *
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

def Ingresarpaciente(request):
	if request.method == "POST":
		form_registro_usuario = IngresarPaciente(request.POST or None)
		if form_registro_usuario.is_valid():
			newPaciente = paciente(id_paciente = request.POST['id_paciente'], Nombre =request.POST['Nombre'],
			Apellido=request.POST['Apellido'],EPS=request.POST['EPS'],Genero=request.POST['Genero'],
			Email=request.POST['Email'],Municipio=request.POST['Municipio'],Edad=request.POST['Edad'])
			newPaciente.save()
	else:
		form_registro_usuario = IngresarPaciente()
	return render(request,'RegistarPaciente.html',{'formulario':form_registro_usuario})

