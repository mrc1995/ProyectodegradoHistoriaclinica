from django.db import models

# Create your models here.

class usuario(models.Model):
	Id_usuario = models.CharField(primary_key=True,max_length=12,unique=True)
	password = models.CharField(max_length=25)	

class paciente(models.Model):
	id_paciente = models.CharField(primary_key=True, max_length=12, unique = True)
	Nombre = models.CharField(max_length = 35)
	Apellido = models.CharField(max_length = 35)
	EPS = models.CharField(max_length = 35)
	Genero = models.CharField(max_length = 35)
	Email = models.CharField(max_length = 35)
	Municipio = models.CharField(max_length = 35)
	Edad = models.CharField (max_length =12)
	Estado_civil = models.CharField(max_length = 25)
	Telefono = models.CharField(max_length = 25)
	Direccion = models.CharField(max_length = 25)
	Religion = models.CharField(max_length = 25)
	Nivel_educativo = models.CharField(max_length = 50)
	Ocupacion = models.CharField(max_length = 25)
	Dia = models.CharField(max_length = 2)
	Mes = models.CharField(max_length = 2)
	Ano = models.CharField(max_length = 4)
	Fecha_atencion = models.CharField(max_length = 50)
	Hora_atencion = models.CharField(max_length = 40)

	def __str__(self):
		return self.id_paciente + self.Nombre + self.Apellido + self.EPS + self.Genero + self.Municipio + self.Edad


class Motivo_consulta(models.Model):
	Id_Motivo = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Motivo_consulta = models.CharField(max_length = 800)

class Para_aportados(models.Model):
	Id_Aporte = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Para_aportados = models.CharField(max_length = 800)

class Antec_fami(models.Model):
	Id_Familiar = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Antec_fami = models.CharField(max_length = 800)

class Enfermedad_Actual(models.Model):
	Id_Enfermedad = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Enf_actual = models.CharField(max_length = 800)


class Gustos_preferencias(models.Model):
	Id_Gustos = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Gustos = models.CharField(max_length = 800)


class Examen_Fisico(models.Model):
	Id_examen = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	TA = models.CharField(max_length=50)
	FC = models.CharField(max_length=50)
	FR = models.CharField(max_length=50)
	Peso = models.CharField(max_length=50)
	Estatura = models.CharField(max_length=50)
	IMC = models.CharField(max_length=50)
	Perimetro_cintura = models.CharField(max_length=50)
	Pulso = models.CharField(max_length=50)
	Aspecto_general = models.CharField(max_length=500)
	Cabeza = models.CharField(max_length=500)
	Cavidad_oral = models.CharField(max_length=500)
	Cuello = models.CharField(max_length=500)
	Cardiopulmonar = models.CharField(max_length=500)
	Abdomen = models.CharField(max_length=500)
	Genitourinario = models.CharField(max_length=500)
	Osteomuscular = models.CharField(max_length=500)
	Piel = models.CharField(max_length=500)
	Neurologico = models.CharField(max_length=500)
	Extremidades = models.CharField(max_length=500)
	Energia = models.CharField(max_length=500)





class Diagnostico(models.Model):
	Id_diag = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Codigo_Nombre= models.CharField(max_length=200)
	Nombre_diag= models.CharField(max_length=400)


class Terapias(models.Model):
	Id_terapia = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Plan_terapeutico= models.CharField(max_length=800)


class Recomendaciones(models.Model):
	Id_recomendacion = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Recomendacion = models.CharField(max_length=800)

class Solicitud_ayudas(models.Model):
	Id_solicitud = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Solicitud_ayudas_diag= models.CharField(max_length=800)



class Antecedentes(models.Model):
	Id_antecedentes = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Patologicos	= models.CharField(max_length=800)
	Farmacologicos = models.CharField(max_length=800)
	Toxicos= models.CharField(max_length=800)
	Alergicos = models.CharField(max_length=800)
	Quirurgicos= models.CharField(max_length=800)
	Trau_fisicos= models.CharField(max_length=800)
	Trau_emocionales= models.CharField(max_length=800)
	Habitos_saludables= models.CharField(max_length=800)
	Habitos_riesgo= models.CharField(max_length=800)


class Rev_sistemas(models.Model):
	Id_revision = models.AutoField(primary_key = True, max_length = 35, unique = True)
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Rev_consulta= models.CharField(max_length=800)


class Paraclinicos(models.Model):
	id_paciente = models.ForeignKey(paciente, null = False, blank = False)
	Id_paraclinico = models.AutoField(primary_key = True, max_length = 35, unique = True)
	Diagnostico= models.CharField(max_length=500)
	Medicamentos= models.CharField(max_length=500)
	Incapacidad= models.CharField(max_length=500)
