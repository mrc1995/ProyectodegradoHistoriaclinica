from django.contrib import admin

# Register your models here.
from Historiaclinica.models import *
admin.site.register(paciente)
admin.site.register(Motivo_consulta)
admin.site.register(Enfermedad_Actual)
admin.site.register(Gustos_preferencias)
admin.site.register(Examen_Fisico)
admin.site.register(medidas_antropometricas)
admin.site.register(Diagnostico)
admin.site.register(Resultado_Examen)
admin.site.register(Terapias)
admin.site.register(Diagnosticos_propios)
admin.site.register(Antecedentes)
admin.site.register(Plan_manejo)
admin.site.register(Rev_sistemas)

