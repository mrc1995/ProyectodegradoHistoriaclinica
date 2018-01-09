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
	id_paciente = forms.CharField(required = True)
	Nombre = forms.CharField(required = True)
	Apellido = forms.CharField(required = True)
	EPS = forms.CharField(required = True)
	Genero = forms.CharField(required = True)
	Email = forms.CharField()
	Municipio = forms.CharField(required = True)
	Edad = forms.CharField(required = True)


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


class Enfermedadactual(forms.ModelForm):

	class Meta:
		model = Enfermedad_Actual
		fields = ('id_paciente','Enf_actual')


class gustos(forms.ModelForm):

	class Meta:
		model = Gustos_preferencias
		fields = ('id_paciente','Clima','Temperatura','Colores','Numeros')

class examen(forms.ModelForm):
    class Meta:
    	model = Examen_Fisico
        fields = ('id_paciente','TA','FC','FR','Peso','Estatura','IMC','Perimetro_cintura','Pulso')

class medidas(forms.ModelForm):
	class Meta:
		model = medidas_antropometricas
		fields = ('Id_examen','Organo','Clasificacion','Especificacion')

class diagnostico(forms.ModelForm):
	class Meta:
		model = Diagnostico
		fields = ('id_paciente','codigo','Nombre','Tipo')

class Resultado_examen(forms.ModelForm):

	class Meta:
		model = Resultado_Examen
		fields = ('id_paciente','Resultado')

class terapias(forms.ModelForm):

	class Meta:
		model = Terapias
		fields = ('id_paciente','Terapia','Estado','Especificaciones')


class diagnosticos_propios(forms.ModelForm):

	class Meta:
		model =Diagnosticos_propios
		fields = ('id_paciente','Nombre_diag')

class antecedentes(forms.ModelForm):

	class Meta: 
		model = Antecedentes
		fields = ('id_paciente','Patologicos_medicamentos','Toxicos_alergicos','Quirurgicos','Trau_fisicos',
			'Trau_emocionales','Habitos_saludables','Habitos_riesgo','Familiares')

class plan(forms.ModelForm):

	class Meta:
		model = Plan_manejo
		fields = ('id_paciente','Plan','Control')

class revision_sistemas(forms.ModelForm):

	class Meta:
		model = Rev_sistemas
		fields = ('id_paciente','Rev_consulta')

class paracli(forms.ModelForm):

	class Meta:
		model =  Paraclinicos
		fields = ('Diagnostico','Medicamentos','Incapacidad')

class BuscarPaciente(forms.Form):
	id_paciente = forms.CharField(required = True)
	Nombre = forms.CharField(required = True)
	Apellido = forms.CharField(required = True)
	EPS = forms.CharField(required = True)
	Genero = forms.CharField(required = True)
	Email = forms.CharField()
	Municipio = forms.CharField(required = True)
	Edad = forms.CharField(required = True)