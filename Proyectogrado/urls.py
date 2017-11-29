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
from Historiaclinica.views import Ingresarpaciente,MotivoConsulta,loginstart,privado,endsesion, EnfermedadActual

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',loginstart, name = 'loginstart'),
     url(r'^loginstart',loginstart, name = 'loginstart'),
    url(r'^privado$',privado,name = 'privado'),
    url(r'^endsesion/$',endsesion,name = 'endsesion'),
    url(r'^Ingresarpaciente',Ingresarpaciente, name = 'Ingresarpaciente'),
    url(r'^MotivoConsulta',MotivoConsulta, name = 'MotivoConsulta'),
    url(r'^EnfermedadActual',EnfermedadActual, name = 'Enfermedad'),
]

