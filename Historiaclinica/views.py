from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def loginstart(request):
	form = loginForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		username= data.get("username")
		password = data.get("password")
		acceso = authenticate(username = username,password = password)
		if acceso is not None:
			if acceso.is_active:
				login(request,acceso)
				return HttpResponseRedirect('/privado')
				#return HttpResponse("Bienvenido {}".format(username))
			else:
				return render(request,'noactivo.html')
		else:
			return render(request,'nousuario.html')
	else:
	 	form = loginForm()
	return render(request, 'login.html')

@login_required(login_url='/ingresar')
def privado(request):
	username = request.user
	return render(request,'privado.html')

@login_required(login_url='/ingresar')
def endsesion(request):
	logout(request)
	return HttpResponseRedirect('/loginstart')

@login_required(login_url='/ingresar')
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

@login_required(login_url='/ingresar')
def MotivoConsulta(request):
	if request.method == "POST":
		form_registro_motivo = Motivoconsulta(request.POST or None)
		print "formulario valido"
		if form_registro_motivo.is_valid():
			print "hola if"
			newMotivo = Motivoconsulta(id_paciente_id = request.POST['id_paciente_id'],Motivo_Consulta=request.POST['Motivo_consulta'])
			newMotivo.save()
			return HttpResponse("Bienvenido {}".format(username))
	else:
		print "estoy en el else"
		form_registro_motivo = Motivoconsulta()
	return render(request,'MotivoConsulta.html')