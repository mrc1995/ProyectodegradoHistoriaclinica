from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from reportlab.pdfgen import canvas
from django.http import HttpResponse
 
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
		form_registro_usuario = IngresarPaciente(request.POST or None)
		if form_registro_usuario.is_valid():
			newPaciente = paciente(id_paciente = request.POST['id_paciente'], Nombre =request.POST['Nombre'],
			Apellido=request.POST['Apellido'],EPS=request.POST['EPS'],Genero=request.POST['Genero'],
			Email=request.POST['Email'],Municipio=request.POST['Municipio'],Edad=request.POST['Edad'])
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
			newGustos = Gustos_preferencias(id_paciente = p, Clima = request.POST['Clima'], Temperatura = request.POST['Temperatura'],Colores = request.POST['Colores'], Numeros = request.POST['Numeros'])
			newGustos.save()
	else:
		form_gustos = gustos()
	return render (request,'Gustos.html') 

@login_required(login_url='/ingresar')
def Examen(request):
	if request.method == "POST":
		form_examen = examen(request.POST or None)
		if form_examen.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newExamen = Examen_Fisico(id_paciente = p, TA = request.POST['TA'], FC = request.POST['FC'],FR = request.POST['FR'], Peso = request.POST['Peso'],
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
			e = Examen_Fisico.objects.get(Id_examen = request.POST['Id_examen'])
			newMedidas = medidas_antropometricas(Id_examen = e, Organo = request.POST['Organo'], Clasificacion = request.POST['Clasificacion'],Especificacion = request.POST['Especificacion'])
			newMedidas.save()
	else:
		form_gustos = medidas()
	return render (request,'Medidas.html') 

@login_required(login_url='/ingresar')
def diagnostico_medico(request):
	if request.method == "POST":
		form_diagnostico = diagnostico(request.POST or None)
		if form_diagnostico.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newDiagnostico = Diagnostico(id_paciente = p, codigo = request.POST['codigo'], Nombre = request.POST['Nombre'],Tipo = request.POST['Tipo'])
			newDiagnostico.save()
	else:
		form_gustos = diagnostico()
	return render (request,'Diagnostico.html') 

@login_required(login_url='/ingresar')
def Resultado(request):
	if request.method == "POST":
		form_resultado = Resultado_examen(request.POST or None)
		if form_resultado.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newResultado = Resultado_Examen(id_paciente = p, Resultado = request.POST['Resultado'])
			newResultado.save()
	else:
		form_gustos = Resultado_examen()
	return render (request,'Resultado_examen.html') 

@login_required(login_url='/ingresar')
def Terapias_new(request):
	if request.method == "POST":
		form_terapia = terapias(request.POST or None)
		if form_terapia.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newTerapia = Terapias(id_paciente = p, Terapia = request.POST['Terapia'],Estado = request.POST['Estado'],Especificaciones = request.POST['Especificaciones'])
			newTerapia.save()
	else:
		form_gustos = terapias()
	return render (request,'Terapias.html') 

@login_required(login_url='/ingresar')
def propios(request):
	if request.method == "POST":
		form_propios = diagnosticos_propios(request.POST or None)
		if form_propios.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newPropios = Diagnosticos_propios(id_paciente = p, Nombre_diag = request.POST['Nombre_diag'])
			newPropios.save()
	else:
		form_gustos = diagnosticos_propios()
	return render (request,'Diagnosticos_propios.html') 

@login_required(login_url='/ingresar')
def recuerdos(request):
	if request.method == "POST":
		form_antecedentes = antecedentes(request.POST or None)
		if form_antecedentes.is_valid():
			p = paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newAntecedentes = Antecedentes(id_paciente = p, Patologicos_medicamentos = request.POST['Patologicos_medicamentos'], Toxicos_alergicos = request.POST['Toxicos_alergicos'],Quirurgicos = request.POST['Quirurgicos'],Trau_fisicos = request.POST['Trau_fisicos'], Trau_emocionales = request.POST['Trau_emocionales'], Habitos_saludables = request.POST['Habitos_saludables'],Habitos_riesgo = request.POST['Habitos_riesgo'], Familiares = request.POST['Familiares'])
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
def plan_de_manejo(request):
	if request.method == "POST":
		form_plan = plan(request.POST or None)
		if form_plan.is_valid():
			p =  paciente.objects.get(id_paciente = request.POST['id_paciente'])
			newPlan = Plan_manejo(id_paciente = p, Plan = request.POST['Plan'], Control = request.POST['Control'])				
			newPlan.save()
	else:
		form_plan = plan()
	return render (request,'Plan_manejo.html')

def registrar_usuario(request):
	if request.method == "POST":
		form_registro = registrar(request.POST or None)
		if form_registro.is_valid():
			NewUsuario = auth_us(username = request.POST['username'],password = request.POST['password'],first_name = request.POST['first_name'],
				last_name = request.POST['last_name'],email = request.POST['email'])
			#NewUsuario.save()
	else:
		form_registro = registrar()
	return render(request,'Registrar.html')


def desplegar(request):
	context = {}
	if request.method == "POST":
		lpaciente = paciente.objects.get(id_paciente = request.POST.get('id_paciente'))
		#lmotivos = Motivo_consulta.objects.filter(id_paciente = request.POST.get('id_paciente'))
		context = {
			"lpaciente": lpaciente,
		#	"lmotivos": lmotivos,
		}
	return render(request, 'list.html', context)

def para(request):
	if request.method == "POST":
		form_para = paracli(request.POST or None)
		if form_para.is_valid():
			Newpara = Paraclinicos(Diagnostico = request.POST['Diagnostico'], Medicamentos = request.POST['Medicamentos'],
			Incapacidad = request.POST['Incapacidad'])
			Newpara.save()
	else:
		form_para = paracli()
	return render(request, 'paraclinicos.html')


def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
 
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
 	
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
 	

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def BuscarHistoria(request):
	context = {}
	if request.method == "POST":
		lpaciente = paciente.objects.get(id_paciente = request.POST.get('id_paciente'))
		motivos = Motivo_consulta.objects.filter(id_paciente = request.POST.get('id_paciente'))
		enfermedad = Enfermedad_Actual.objects.filter(id_paciente = request.POST.get('id_paciente'))
		gustos = Gustos_preferencias.objects.filter(id_paciente = request.POST.get('id_paciente'))
		examen = Examen_Fisico.objects.filter(id_paciente = request.POST.get('id_paciente'))
		#medidas = medidas_antropometricas.objects.filter(id_paciente = request.POST.get('id_paciente'))
		diagnostico = Diagnostico.objects.filter(id_paciente = request.POST.get('id_paciente'))
		resultado = Resultado_Examen.objects.filter(id_paciente = request.POST.get('id_paciente'))
		terapia = Terapias.objects.filter(id_paciente = request.POST.get('id_paciente'))
		propios =Diagnosticos_propios.objects.filter(id_paciente = request.POST.get('id_paciente'))
		antecedentes = Antecedentes.objects.filter(id_paciente = request.POST.get('id_paciente'))
		plan = Plan_manejo.objects.filter(id_paciente = request.POST.get('id_paciente'))
		revision = Rev_sistemas.objects.filter(id_paciente = request.POST.get('id_paciente'))
		context = {
			"lpaciente": lpaciente,
			"motivos": motivos,
			"enfermedad": enfermedad,
			"gustos":gustos,
			"examen":examen,
			#"medidas":medidas,
			"diagnostico":diagnostico,
			"resultado":resultado,
			"terapia":terapia,
			"propios":propios,
			"antecedentes":antecedentes,
			"plan":plan,
			"revision":revision,
		}
	return render(request, 'Historiaclinica.html', context)