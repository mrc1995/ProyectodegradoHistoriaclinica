from django import forms


class loginForm(forms.Form):
	username = forms.CharField(max_length=25,required = True,
		widget=(forms.TextInput(attrs={"placeholder":"CC","class":"input-login"})))
	password = forms.CharField(max_length=25,required = True,
		widget=(forms.TextInput(attrs={"placeholder":"Contrasena","class":"input-login"})))

