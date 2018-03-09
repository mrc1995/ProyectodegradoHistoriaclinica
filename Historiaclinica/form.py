from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *




class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',	
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}



class loginForm(forms.Form):
	username = forms.CharField(max_length=25,required = True)
	password = forms.CharField(max_length=25,required = True)


"""class registrar(forms.Form):
	username = forms.CharField(max_length=25,required = True)
	password = forms.CharField(max_length=25,required = True)
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.CharField()"""

class IngresarPaciente(forms.Form):
	Fecha_atencion = forms.CharField(required = False)
	Hora_atencion = forms.CharField(required = False)
	id_paciente = forms.CharField(required = True)
	Nombre = forms.CharField(required = True)
	Apellido = forms.CharField(required = True)
	EPS = forms.CharField(required = False)
	Genero = forms.CharField(required = False)
	Email = forms.CharField(required = False)
	Municipio = forms.CharField(required = False)
	Edad = forms.CharField(required = False)
	Estado_civil = forms.CharField(required = False)
	Telefono = forms.CharField(required = False)
	Direccion = forms.CharField(required = False)
	Religion = forms.CharField(required = False)
	Nivel_educativo = forms.CharField(required = False)
	Ocupacion = forms.CharField(required = False)
	Dia = forms.CharField(required = False)
	Mes = forms.CharField(required = False)
	Ano = forms.CharField(required = False)



class modificar_paciente(forms.Form):
	id_paciente = forms.CharField(required = True)
	Nombre = forms.CharField(required = True)
	Apellido = forms.CharField(required = True)
	EPS = forms.CharField(required = True)
	Genero = forms.CharField(required = True)
	Email = forms.CharField()
	Municipio = forms.CharField(required = True)
	Edad = forms.CharField(required = True)


class paracli(forms.ModelForm):

	class Meta:
		model =  Paraclinicos
		fields = ('id_paciente','Diagnostico','Medicamentos','Incapacidad')


class Motivoconsulta(forms.ModelForm):

	class Meta:
		model = Motivo_consulta
		fields = ('id_paciente','Motivo_consulta')

class Antecfami(forms.ModelForm):

	class Meta:
		model = Antec_fami
		fields = ('id_paciente','Antec_fami')


class Paraaportados(forms.ModelForm):

	class Meta:
		model = Para_aportados
		fields = ('id_paciente','Para_aportados')


class Enfermedadactual(forms.ModelForm):

	class Meta:
		model = Enfermedad_Actual
		fields = ('id_paciente','Enf_actual')


class gustos(forms.ModelForm):

	class Meta:
		model = Gustos_preferencias
		fields = ('id_paciente','Gustos')

class Examen(forms.ModelForm):
    class Meta:
    	model = Examen_Fisico
        fields = ('id_paciente','TA','FC','FR','Peso','Estatura','IMC','Perimetro_cintura','Pulso','Aspecto_general',
        	'Cabeza','Cavidad_oral','Cuello','Cardiopulmonar','Abdomen','Genitourinario','Osteomuscular','Piel',
        	'Neurologico','Extremidades','Energia')



class diagnostico(forms.ModelForm):
	class Meta:
		model = Diagnostico
		fields = ('id_paciente','Codigo_Nombre','Nombre_diag')



class terapias(forms.ModelForm):

	class Meta:
		model = Terapias
		fields = ('id_paciente','Plan_terapeutico')


class antecedentes(forms.ModelForm):

	class Meta: 
		model = Antecedentes
		fields = ('id_paciente','Patologicos', 'Farmacologicos','Toxicos','Alergicos','Quirurgicos','Trau_fisicos',
			'Trau_emocionales','Habitos_saludables','Habitos_riesgo')


class revision_sistemas(forms.ModelForm):

	class Meta:
		model = Rev_sistemas
		fields = ('id_paciente','Rev_consulta')

class paracli(forms.ModelForm):

	class Meta:
		model =  Paraclinicos
		fields = ('Diagnostico','Medicamentos','Incapacidad')


class recomendaciones(forms.ModelForm):

	class Meta:
		model =  Recomendaciones
		fields = ('id_paciente','Recomendacion')

class solicitud_ayudas_diag(forms.ModelForm):

	class Meta:
		model =  Solicitud_ayudas
		fields = ('id_paciente','Solicitud_ayudas_diag')




class BuscarPaciente(forms.Form):
	id_paciente = forms.CharField(required = True)
	Nombre = forms.CharField(required = True)
	Apellido = forms.CharField(required = True)
	EPS = forms.CharField(required = True)
	Genero = forms.CharField(required = True)
	Email = forms.CharField()
	Municipio = forms.CharField(required = True)
	Edad = forms.CharField(required = True)