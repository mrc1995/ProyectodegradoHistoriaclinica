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
	return render(request,'base.html')

@login_required(login_url='/ingresar')
def endsesion(request):
	logout(request)
	return HttpResponseRedirect('/loginstart')

@login_required(login_url='/ingresar')
def Ingresarpaciente(request):
	if request.method == "POST":
		print "estoy despues del if"
		form_registro_usuario = IngresarPaciente(request.POST or None)
		if form_registro_usuario.is_valid():
			print "estoy despues del if"
			newPaciente = paciente(id_paciente = request.POST['id_paciente'], Nombre =request.POST['Nombre'],
			Apellido=request.POST['Apellido'],EPS=request.POST['EPS'],Genero=request.POST['Genero'],
			Email=request.POST['Email'],Municipio=request.POST['Municipio'],Edad=request.POST['Edad'])
			print "Paciente ingresado"
			newPaciente.save()
	else:
		form_registro_usuario = IngresarPaciente()
	return render(request,'RegistarPaciente.html')

@login_required(login_url='/ingresar')
def MotivoConsulta(request):
	if request.method == "POST":
		form_registro_motivo = Motivoconsulta(request.POST or None)
		if form_registro_motivo.is_valid():
			paciente =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			print p.Nombre
			newMotivo = Motivo_consulta(id_paciente = paciente, Motivo_consulta=request.POST['Motivo_consulta'])
			newMotivo.save()
	else:
		form_registro_motivo = Motivoconsulta()
	return render(request,'MotivoConsulta.html')

@login_required(login_url='/ingresar')
def EnfermedadActual(request):
	if request.method == "POST":
		form_enfermedad = Enfermedadactual(request.POST or None)
		if form_enfermedad.is_valid():
			paciente =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newEnfermedad = Enfermedad_Actual(id_paciente = paciente, Enf_actual = request.POST['Enf_actual'])
			newEnfermedad.save()
	else: 
		form_enfermedad = Enfermedadactual()
	return render(request, 'EnfermedadActual.html')

@login_required(login_url='/ingresar')
def gustos_paciente(request):
	if request.method == "POST":
		form_gustos = gustos(request.POST or None)
		if form_gustos.is_valid():
			paciente =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newGustos = Gustos_preferencias(id_paciente = paciente, Clima = request.POST['Clima'], Temperatura = request.POST['Temperatura'],Colores = request.POST['Colores'], Numeros = request.POST['Numeros'])
			newGustos.save()
	else:
		form_gustos = gustos()
	return render (request,'Gustos.html') 

@login_required(login_url='/ingresar')
def Examen(request):
	if request.method == "POST":
		form_examen = examen(request.POST or None)
		if form_examen.is_valid():
			paciente =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newExamen = Examen_fisico(id_paciente = paciente, TA = request.POST['TA'], FC = request.POST['FC'],FR = request.POST['FR'], Peso = request.POST['Peso'],
				Estatura =request.POST['Estatura'],Perimetro_cintura = request.POST['Perimetro_cintura'],IMC = request.POST['IMC'],Pulso = request.POST['Pulso'] )
			newExamen.save()
	else:
		form_gustos = examen()
	return render (request,'Examen.html') 

@login_required(login_url='/ingresar')
def Medidas(request):
	if request.method == "POST":
		form_medidas = medidas(request.POST or None)
		if form_medidas.is_valid():
			examen = paciente.objects.get(id_examen = request.POST['id_examen'])
			newMedidas = medidas_antropometricas(id_examen = examen, Organo = request.POST['Organo'], Clasificacion = request.POST['Clasificacion'],Especificacion = request.POST['Expecificacion'])
			newMedidas.save()
	else:
		form_gustos = medidas()
	return render (request,'Medidas.html') 

@login_required(login_url='/ingresar')
def Diagnostico(request):
	if request.method == "POST":
		form_diagnostico = diagnostico(request.POST or None)
		if form_diagnostico.is_valid():
			paciente =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newDiagnostico = Diagnostico(id_paciente = paciente, Codigo = request.POST['Codigo'], Nombre = request.POST['Nombre'],Tipo = request.POST['Tipo'])
			newDiagnostico.save()
	else:
		form_gustos = diagnostico()
	return render (request,'Diagnostico.html') 

@login_required(login_url='/ingresar')
def Resultado(request):
	if request.method == "POST":
		form_resultado = Resultado_examen(request.POST or None)
		if form_resultado.is_valid():
			paciente = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newResultado = Resultado_Examen(id_paciente = paciente, Resultado = request.POST['Resultado'])
			newResultado.save()
	else:
		form_gustos = Resultado_examen()
	return render (request,'Resultado_examen.html') 

@login_required(login_url='/ingresar')
def Terapias_new(request):
	if request.method == "POST":
		form_terapia = terapias(request.POST or None)
		if form_terapia.is_valid():
			paciente = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newTerapia = Terapias(id_paciente = paciente, Terapia = request.POST['Terapia'],Estado = request.POST['Estado'],Espeficaciones = request.POST['Especificaciones'])
			newTerapia.save()
	else:
		form_gustos = terapias()
	return render (request,'Terapias.html') 

@login_required(login_url='/ingresar')
def Diagnosticos_propios(request):
	if request.method == "POST":
		form_propios = diagnosticos_propios(request.POST or None)
		if form_propios.is_valid():
			paciente = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newPropios = Diagnosticos_propios(id_paciente = paciente, Nombre_diag = request.POST['Nombre_diag'])
			newPropios.save()
	else:
		form_gustos = diagnosticos_propios()
	return render (request,'Diagnosticos_propios.html') 


###############################33


@login_required(login_url='/ingresar')
def Diagnosticos_propios(request):
	if request.method == "POST":
		form_propios = diagnosticos_propios(request.POST or None)
		if form_propios.is_valid():
			paciente = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newPropios = Diagnosticos_propios(id_paciente = paciente, Nombre_diag = request.POST['Nombre_diag'])
			newPropios.save()
	else:
		form_gustos = diagnosticos_propios()
	return render (request,'Diagnosticos_propios.html') 