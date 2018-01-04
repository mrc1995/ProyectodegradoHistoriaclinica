"""Proyectogrado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Historiaclinica.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',loginstart, name = 'loginstart'),
    url(r'^loginstart',loginstart, name = 'loginstart'),
    url(r'^privado$',privado,name = 'privado'),
    url(r'^endsesion/$',endsesion,name = 'endsesion'),
    url(r'^Ingresarpaciente',Ingresarpaciente, name = 'Ingresarpaciente'),
    url(r'^MotivoConsulta',MotivoConsulta, name = 'MotivoConsulta'),
    url(r'^EnfermedadActual',EnfermedadActual, name = 'Enfermedad'),
    url(r'^gustos_paciente',gustos_paciente, name = 'Gustos'),
    url(r'^Examen',Examen,name='Examen'),
    url(r'^Medidas',Medidas,name ='Medidas_antropometricas'),
    url(r'^diagnostico_medico', diagnostico_medico, name='diagnostico_medico'),
    url(r'^Resultado', Resultado, name='Resultado'),
    url(r'^Terapias_new', Terapias_new, name = 'Terapias'),
    url(r'^propios', propios, name='propios'),
    url(r'^recuerdos', recuerdos, name='hola'),
    url(r'^plan_de_manejo', plan_de_manejo, name= 'Plan'),
    url(r'^Revision_sistemas', Revision_sistemas, name= 'Revision'),
    url(r'^registrar', RegistroUsuario.as_view(), name = 'Registrar'),
    #rl(r'^desplegar', desplegar, name = 'desplegar'),
    url(r'^BuscarHistoria', BuscarHistoria, name = 'BuscarHistoria'),
    url(r'^menu', menu, name = 'menu'),
    url(r'^cabecera', cabecera, name = 'cabecera'),
    url(r'^items', items, name = 'items'),
    url(r'^contenido', contenido, name = 'contenido'),
    url(r'^modificar',modificar,name = 'modificar'),
    url(r'^individuales',individuales,name= 'individuales'),
    url(r'^paraclinicos',paraclinicos,name = 'paraclinicos'),
    url(r'^no_existe',no_existe,name = 'no_existe'),
]

