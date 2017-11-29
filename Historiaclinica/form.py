from django.forms import ModelForm
from django import forms
from .models import *

class loginForm(forms.Form):
	username = forms.CharField(max_length=25,required = True)
	password = forms.CharField(max_length=25,required = True)


class IngresarPaciente(forms.Form):
	id_paciente = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Documento Identidad"})))
	Nombre = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Nombre"})))
	Apellido = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Apellido"})))
	EPS = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"EPS"})))
	Genero = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Genero"})))
	Email = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Email"})))
	Municipio = forms.CharField(required = True)
	Edad = forms.CharField(required = True)

class Motivoconsulta(forms.ModelForm):

	class Meta:
		model = Motivo_consulta
		fields = ('id_paciente','Motivo_consulta')


class Enfermedadactual(forms.ModelForm):

	class Meta:
		model = Enfermedad_Actual
		fields = ('id_paciente','Enf_actual')