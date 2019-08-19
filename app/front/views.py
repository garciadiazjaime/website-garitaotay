from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from django.template import RequestContext
from app.front.lang import Lang
from app.front.menu import Menu
from app.front.tramites import Tramites
from app.front.seguros import Seguros
from app.front.permisos import Permisos
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import re

lang = Lang()
menu = Menu()


def inicio(request, ln=0, category=''):	
	if ln == 0:	
		data = lang.inicio()
		es_active = "active"
	else:
		data = lang.home()		
		en_active = "active"
	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)
	return render_to_response('sections/home.html', locals())

def nosotros(request, ln=0, category=''):	
	if ln == 0:	
		data = lang.nosotros()
		es_active = "active"
	else:
		data = lang.about_us()		
		en_active = "active"

	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)
	return render_to_response('sections/nosotros.html', locals())

def tramites_permisos(request, ln=0, category=''):	
	tramites = Tramites()	
	dmv = tramites.dmv(ln)	
	eu = tramites.eu(ln)
	mx = tramites.mx(ln) 	
	if ln == 0:	
		data = lang.tramites_permisos()
		es_active = "active"
	else:
		data = lang.procedures()
		en_active = "active"

	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)
	return render_to_response('sections/tramites_permisos.html', locals())

def permisos(request, ln=0, category=''):
	permisos = Permisos()	
	eu = permisos.eu(ln)
	if ln == 0:	
		data = lang.permisos()
		es_active = "active"
	else:
		data = lang.permits()
		en_active = "active"

	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)

	return render_to_response('sections/permisos.html', locals())

def seguros(request, ln=0, category=''):
	seguros = Seguros()
	eu = seguros.eu(ln)	
	mx = seguros.mx(ln)
	if ln == 0:	
		data = lang.seguros()
		es_active = "active"
	else:
		data = lang.insurance()
		en_active = "active"
	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)
	return render_to_response('sections/seguros.html', locals())

def auditorias(request, ln=0, category=''):
	if ln == 0:
		data = lang.auditorias()
		es_active = "active"
	else:
		data = lang.audits()
		en_active = "active"
	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)

	return render_to_response('sections/auditorias.html', locals())

def compra_linea(request, ln=0):
	if ln == 0:
		data = lang.compra_linea()
		es_active = "active"
	else:
		data = lang.buy_online()
		en_active = "active"
	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)

	return render_to_response('sections/compra_linea.html', locals())

@csrf_exempt
def contacto(request, ln=0):
	if ln == 0:
		data = lang.contacto()
		es_active = "active"
	else:
		data = lang.contact()
		en_active = "active"
	main_menu = menu.get_main_menu(data['info_gral']['section'], ln)

	return render_to_response('sections/contacto.html', locals())

@csrf_exempt
def my_send_mail(request):
	name = request.POST.get('name', '')
	email = request.POST.get('email', '')
	tel = request.POST.get('tel', '')
	service = request.POST.get('select_service', '')
	message = request.POST.get('message', '')
	response = ''
	msg = ''
	if len(name) == 0 or len(email) == 0 or len(message) == 0:
		response = 'empty_data'
	elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
  		response = 'invalid_email'
	else:
		msg = "Name: " + name + "\n"
		msg += "Email: " + email + "\n"
		msg += "Telephone: " + tel + "\n"
		msg += "Service: " + service + "\n"
		msg += "Message: " + message + "\n"
		try:
			send_mail('Forma de Contacto Website', msg, email, ['info.mintitmedia@gmail.com'])
			response = 'success'
		except:
			response = "error"

	return HttpResponse(response)
