from django.forms import ModelForm
from django import forms
from .models import *

class loginForm(forms.Form):
	username = forms.CharField(max_length=25,required = True,
		widget=(forms.TextInput(attrs={"placeholder":"Nombre de usuario","class":"input-login"})))
	password = forms.CharField(max_length=25,required = True,
		widget=(forms.TextInput(attrs={"placeholder":"Contrasena","class":"input-login"})))


class IngresarPaciente(forms.Form):
	id_paciente = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Documento Identidad"})))
	Nombre = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Nombre"})))
	Apellido = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Apellido"})))
	EPS = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"EPS"})))
	Genero = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Genero"})))
	Email = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Email"})))
	Municipio = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Municipio"})))
	Edad = forms.CharField(required = True, widget =(forms.TextInput(attrs = {"placheholder":"Edad"})))

	