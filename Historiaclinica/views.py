from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .form import RegistroForm
from django.views.generic import View
from io import BytesIO


class RegistroUsuario(CreateView):
	model = User
	template_name = "Registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('loginstart')


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
				return HttpResponseRedirect('/menu')
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
		form_registro_usuario = IngresarPaciente(request.POST or None)
		if form_registro_usuario.is_valid():
			newPaciente = paciente(id_paciente = request.POST['id_paciente'], Nombre =request.POST['Nombre'],
			Apellido=request.POST['Apellido'],EPS=request.POST['EPS'],Genero=request.POST['Genero'],
			Email=request.POST['Email'],Municipio=request.POST['Municipio'],Edad=request.POST['Edad'],Estado_civil=request.POST['Estado_civil'],
			Telefono=request.POST['Telefono'],Direccion=request.POST['Direccion'],Religion=request.POST['Religion'], Nivel_educativo = request.POST['Educativo'], Ocupacion=request.POST['Ocupacion'],Dia=request.POST['Dia'],
			Mes=request.POST['Mes'],Ano=request.POST['Ano'], Fecha_atencion = request.POST ['Fecha'], Hora_atencion = request.POST ['Hora'])
			newPaciente.save()
	else:
		form_registro_usuario = IngresarPaciente()
	return render(request,'RegistarPaciente.html')

@login_required(login_url='/ingresar')
def MotivoConsulta(request):
	if request.method == "POST":
		form_registro_motivo = Motivoconsulta(request.POST or None)
		if form_registro_motivo.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			print p.Nombre
			newMotivo = Motivo_consulta(id_paciente = p, Motivo_consulta=request.POST['Motivo_consulta'])
			newMotivo.save()
	else:
		form_registro_motivo = Motivoconsulta()
	return render(request,'MotivoConsulta.html')


@login_required(login_url='/ingresar')
def Examen_fis(request):
	if request.method == "POST":
		form_examen = Examen(request.POST or None)
		if form_examen.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newExamen = Examen_Fisico(id_paciente = p, TA = request.POST['TA'], FC = request.POST['FC'],FR = request.POST['FR'], Peso = request.POST['Peso'],
				Estatura =request.POST['Estatura'],IMC = request.POST['IMC'],Perimetro_cintura = request.POST['Perimetro_cintura'],Pulso = request.POST['Pulso'], 
				Aspecto_general = request.POST['Aspecto_general'],Cabeza  = request.POST['Cabeza'],Cavidad_oral = request.POST['Cavidad_oral'],Cuello = request.POST['Cuello'],Cardiopulmonar = request.POST['Cardiopulmonar'],
				Abdomen = request.POST['Abdomen'],Genitourinario = request.POST['Genitourinario'],Osteomuscular = request.POST['Osteomuscular'],Piel  = request.POST['Piel'],Neurologico = request.POST['Neurologico'],
				Extremidades = request.POST['Extremidades'], Energia = request.POST['Energia'])
			newExamen.save()
	else:
		form_examen = Examen()
	return render (request,'Examen.html') 



@login_required(login_url='/ingresar')
def AntecFami(request):
	if request.method == "POST":
		form_familiar = Antecfami(request.POST or None)
		if form_familiar.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newFami = Antec_fami(id_paciente = p, Antec_fami=request.POST['Antec_fami'])
			newFami.save()
	else:
		form_familiar = Antec_fami()
	return render(request,'Anteced_Familiares.html')


@login_required(login_url='/ingresar')
def ParaAportados(request):
	if request.method == "POST":
		form_aportados = Paraaportados(request.POST or None)
		if form_aportados.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newPara = Para_aportados(id_paciente = p, Para_aportados=request.POST['Para_aportados'])
			newPara.save()
	else:
		form_aportados = Para_aportados()
	return render(request,'Aportados.html')


@login_required(login_url='/ingresar')
def EnfermedadActual(request):
	if request.method == "POST":
		form_enfermedad = Enfermedadactual(request.POST or None)
		if form_enfermedad.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newEnfermedad = Enfermedad_Actual(id_paciente = p, Enf_actual = request.POST['Enf_actual'])
			newEnfermedad.save()
	else: 
		form_enfermedad = Enfermedadactual()
	return render(request, 'EnfermedadActual.html')



@login_required(login_url='/ingresar')
def gustos_paciente(request):
	if request.method == "POST":
		form_gustos = gustos(request.POST or None)
		if form_gustos.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newGustos = Gustos_preferencias(id_paciente = p, Gustos = request.POST['Gustos'])
			newGustos.save()
	else:
		form_gustos = gustos()
	return render (request,'Gustos.html') 



@login_required(login_url='/ingresar')
def diagnostico_medico(request):
	if request.method == "POST":
		form_diagnostico = diagnostico(request.POST or None)
		if form_diagnostico.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newDiagnostico = Diagnostico(id_paciente = p, Codigo_Nombre = request.POST['Codigo_Nombre'], Nombre_diag = request.POST['Nombre_diag'])
			newDiagnostico.save()
	else:
		form_gustos = diagnostico()
	return render (request,'Diagnostico.html')



@login_required(login_url='/ingresar')
def Terapias_new(request):
	if request.method == "POST":
		form_terapia = terapias(request.POST or None)
		if form_terapia.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newTerapia = Terapias(id_paciente = p, Plan_terapeutico = request.POST['Plan_terapeutico'])
			newTerapia.save()
	else:
		form_gustos = terapias()
	return render (request,'Terapias.html') 



@login_required(login_url='/ingresar')
def recuerdos(request):
	if request.method == "POST":
		form_antecedentes = antecedentes(request.POST or None)
		if form_antecedentes.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newAntecedentes = Antecedentes(id_paciente = p, Patologicos = request.POST['Patologicos'], Farmacologicos = request.POST['Farmacologicos'], Toxicos = request.POST['Toxicos'], Alergicos = request.POST['Alergicos'], Quirurgicos = request.POST['Quirurgicos'],Trau_fisicos = request.POST['Trau_fisicos'], Trau_emocionales = request.POST['Trau_emocionales'], Habitos_saludables = request.POST['Habitos_saludables'],Habitos_riesgo = request.POST['Habitos_riesgo'])
			newAntecedentes.save()
	else:
		form_antecedentes = antecedentes()
	return render (request,'Antecedentes.html') 


@login_required(login_url='/ingresar')
def Revision_sistemas(request):
	if request.method == "POST":
		form_revision = revision_sistemas(request.POST or None)
		if form_revision.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newRevision = Rev_sistemas(id_paciente = p, Rev_consulta = request.POST['Rev_consulta'])
			newRevision.save()
	else:
		form_revision = revision_sistemas()
	return render (request,'Revision_sistemas.html')




@login_required(login_url='/ingresar')
def Recomendacion(request):
	if request.method == "POST":
		form_recomendacion_medica = recomendaciones(request.POST or None)
		if form_recomendacionmedica.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newRecomendacionmedica = Recomendaciones(id_paciente = p, Recomendacion = request.POST['Recomendacion'])
			newRecomendacionmedica.save()
	else:
		form_recomendacionmedica = recomendaciones()
	return render (request,'Recomendaciones.html') 

@login_required(login_url='/ingresar')
def Solicitud(request):
	if request.method == "POST":
		form_solicitudayudas = solicitud_ayudas_diag(request.POST or None)
		if form_solicitudayudas.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newSolicitudayudas = Solicitud_ayudas_diag(id_paciente = p, Solicitud_ayudas_diag = request.POST['Solicitud_ayudas_diag'])
			newSolicitudayudas.save()
	else:
		form_solicitudayudas = solicitud_ayudas_diag()
	return render (request,'Solicitudes.html') 





@login_required(login_url='/ingresar')
def paraclinicos(request):
	context = {}
	if request.method == "POST":
		try:
			lpaciente = paciente.objects.get(id_paciente = request.POST.get('id_paciente'))
			paraclinicos = Paraclinicos.objects.filter(id_paciente = request.POST.get('id_paciente'))
			context = {"lpaciente": lpaciente,
					"paraclinicos": paraclinicos,
			}
		except:
			return HttpResponseRedirect('no_existe')
	return render(request, 'paraclinicos.html',context)

def no_existe(request):
	return render(request,'noexiste.html')


@login_required(login_url='/ingresar')
def individuales(request):
	if request.method == "POST":
		form_para = paracli(request.POST or None)
		if form_para.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			Newpara = Paraclinicos(id_paciente = p,Diagnostico = request.POST['Diagnostico'], Medicamentos = request.POST['Medicamentos'],
			Incapacidad = request.POST['Incapacidad'])
			Newpara.save()
	else:
		form_para = paracli()
	return render(request, 'paraclinicos_individuales.html')

@login_required(login_url='/ingresar')
def BuscarHistoria(request):
	context = {}
	if request.method == "POST":
		try:
			lpaciente = paciente.objects.get(id_paciente = request.POST.get('id_paciente'))
			motivos = Motivo_consulta.objects.filter(id_paciente = request.POST.get('id_paciente'))
			enfermedad = Enfermedad_Actual.objects.filter(id_paciente = request.POST.get('id_paciente'))
			gustos = Gustos_preferencias.objects.filter(id_paciente = request.POST.get('id_paciente'))
			examen = Examen_Fisico.objects.filter(id_paciente = request.POST.get('id_paciente'))
			diagnostico = Diagnostico.objects.filter(id_paciente = request.POST.get('id_paciente'))
			terapia = Terapias.objects.filter(id_paciente = request.POST.get('id_paciente'))
			antecedentes = Antecedentes.objects.filter(id_paciente = request.POST.get('id_paciente'))
			revision = Rev_sistemas.objects.filter(id_paciente = request.POST.get('id_paciente'))
			aportados = Para_aportados.objects.filter(id_paciente = request.POST.get('id_paciente'))
			familiares = Antec_fami.objects.filter(id_paciente = request.POST.get('id_paciente'))
			recomendacion = Recomendaciones.objects.filter(id_paciente = request.POST.get('id_paciente'))
			solicitud = Solicitud_ayudas.objects.filter(id_paciente = request.POST.get('id_paciente'))
			context = {
				"lpaciente": lpaciente,
				"motivos": motivos,
				"enfermedad": enfermedad,
				"gustos":gustos,
				"examen":examen,
				"diagnostico":diagnostico,
				"terapia":terapia,
				"antecedentes":antecedentes,
				"revision":revision,
				"aportados":aportados,
				"familiares":familiares,
				"recomendacion":recomendacion,
				"solicitud":solicitud,

			}
		except:
			return HttpResponseRedirect('no_existe')
	return render(request, 'Historiaclinica.html', context)

@login_required(login_url='/ingresar')
def menu(request):
	username = request.user
	return render(request,'menu.html')

@login_required(login_url='/ingresar')
def cabecera(request):
	username = request.user
	return render(request,'cabecera.html')

@login_required(login_url='/ingresar')
def items(request):
	username = request.user
	return render(request,'items.html')

@login_required(login_url='/ingresar')
def contenido(request):
	username = request.user
	return render(request,'contenido.html')


@login_required(login_url='/ingresar')
def modificar(request):
	context = {}
	if request.method == "POST":
		try:
			lpaciente = paciente.objects.get(id_paciente = request.POST.get('id_paciente'))
			context = {"lpaciente": lpaciente}
			form_modificar = modificar_paciente(request.POST or None)
		#print "aqui estoy"
			if form_modificar.is_valid():
			#print "aqui despues del if"
				modpaciente = paciente(id_paciente = request.POST['id_paciente'], Nombre =request.POST['Nombre'],
				Apellido=request.POST['Apellido'],EPS=request.POST['EPS'],Genero=request.POST['Genero'],
				Email=request.POST['Email'],Municipio=request.POST['Municipio'],Edad=request.POST['Edad'])
				modpaciente.save()
		except:
			return HttpResponseRedirect('no_existe')
	else:
		form_modificar = modificar_paciente()

	return render(request,'modificar.html',context)


       

