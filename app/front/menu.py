# -*- coding: utf-8 -*-



class Menu(object):

	items = [
		[			
			{				
				'href': 'inicio',
				'title': 'Inicio',
				'extra': '<h1><span class="first">Su Mejor Alternativa</span><span>en <strong>Trámites y Permisos</span></strong></h1>',
			},
			{				
				'href': 'nosotros',
				'title': 'Nosotros',
				'extra': '<h1>Nosotros</h1>',
				'child':[
					{
						'href': 'quienes-somos',
						'title': 'Quiénes somos',
					},
					{
						'href': 'mision-vision',
						'title': 'Misión y Visión',
					},
					{
						'href': 'valores',
						'title': 'Valores',
					},
					{
						'href': 'ventajas-competitivas',
						'title': 'Ventajas Competitivas',
					},
					{
						'href': 'responsabilidad_social',
						'title': 'responsabilidad social',
					},
					{
						'href': 'nuestros_clientes',
						'title': 'Nuestros Clientes',
					},
					{
						'href': 'companias-aseguradoras',
						'title': 'Compañías de seguros que representamos',
					},
				]
			},
			{				
				'href': 'tramites',
				'title': 'Trámites y permisos',
				'extra': '<h1>Trámites y Permisos</h1>',
				'child':[
					{
						'href': 'tramites',
						'title': 'Trámites',
						'child':[
							{
								'href': 'dmv',
								'title': 'Trámites DMV',
							},
							{
								'href': 'eu',
								'title': 'Trámites en E.U.',
							},
							{
								'href': 'mexico',
								'title': 'Trámites en México',
							},
						]
					},
					{
						'href': 'permisos',
						'title': 'Permisos',
						'child':[
							{
								'href': 'eu',
								'title': 'Permisos en E.U.',
							},
						]
					},
				]
			},
			{				
				'href': 'seguros',
				'title': 'Seguros',
				'extra': '<h1>Seguros</h1>',
				'child':[
					{
						'href': 'eu',
						'title': 'Seguros en E.U.',
					},
					{
						'href': 'mexico',
						'title': 'Seguros en México',
					},					
				]				
			},
			{				
				'href': 'auditorias',
				'title': 'Auditorías',
				'extra': '<h1>Auditorías<span class="small_text">Servicio de consultoría en auditorías</span></h1>'
			},
			{				
				'href': 'compra_linea',
				'title': 'Compra en Línea',
				'extra': '<h1>Compra en línea</h1>'
			},
			{				
				'href': 'contacto',
				'title': 'Contacto',
				'extra': '<h1>Contacto</h1>'
			},			
		],			
		################################ ENGLISH ################################

		[
			{				
				'href': 'home',
				'title': 'Home',
				'extra': '<h1><span class="first">Su Mejor Alternativa</span><span>en <strong>Trámites y Permisos</span></strong></h1>',
			},
			{				
				'href': 'about-us',
				'title': 'About us',
				'extra': '<h1>Nosotros</h1>',
				'child':[
					{
						'href': 'quienes-somos',
						'title': 'Quiénes somos',
					},
					{
						'href': 'mission-vision',
						'title': 'Mission y Vision',
					},
					{
						'href': 'values',
						'title': 'Values',
					},
					{
						'href': 'competitive advantages',
						'title': 'Comptetitive Advantages',
					},
					{
						'href': 'our_clients',
						'title': 'Our Clients',
					},
					{
						'href': 'insurance-companies',
						'title': ' Insurance Companies we Represent',
					},
				]
			},
			{				
				'href': 'procedures',
				'title': 'Procedures and permits',
				'extra': '<h1>Procedures and permits</h1>',
				'child':[
					{
						'href': 'procedures',
						'title': 'Procedures',
						'child':[
							{
								'href': 'dmv',
								'title': 'DMV paperwork',
							},
							{
								'href': 'us',
								'title': 'Proceedings in the U.S.',
							},
							{
								'href': 'mexico',
								'title': 'Proceedings in Mexico',
							},
						]
					},
					{
						'href': 'permits',
						'title': 'Permits',
						'child':[
							{
								'href': 'us',
								'title': 'Permits in U.S.',
							},
						]
					},
				]
			},
			{				
				'href': 'insurance',
				'title': 'Insurance',
				'extra': '<h1>Insurance</h1>',
				'child':[
					{
						'href': 'eu',
						'title': 'Insurance in the U.S.',
					},
					{
						'href': 'mexico',
						'title': 'Insurance in Mexico',
					},					
				]				
			},
			{				
				'href': 'audits',
				'title': 'Audits',
				'extra': '<h1>Auditorías<span class="small_text">Servicio de consultoría en auditorías</span></h1>'
			},
			{				
				'href': 'buy_online',
				'title': 'Buy online',
				'extra': '<h1>Buy online</h1>'
			},
			{				
				'href': 'contact',
				'title': 'Contact',
				'extra': '<h1>Contact</h1>'
			},				
		],
	]




	def get_main_menu(self, section, lang):
		response = ''		
		for row in self.items[lang]:
			if row['href'] == section:
				response += "<li id=\"m_"+row['href']+"\" class=\"active \"><a href=\"/"+row['href']+"\" title=\"/"+row['title'] +"\"><span>"+row['title']+"</span></a></li>"
			else:
				response += "<li id=\"m_"+row['href']+"\"><a href=\"/"+row['href']+"\" title=\"/"+row['title'] +"\"><span>"+row['title']+"</span></a></li>"

		if len(response):
			response = "<ul class=\"menu\">" + response + "</ul>"
		return response		


	def get_footer(self, section):
		response = ''		
		for row in self.items:
			if row['href'] not in 'testimoniales,contacto':
				child = self.get_child(row['href'], row['child']) if row.has_key('child') else ''
				if row['href'] == section:
					response += "<li class=\"active \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a> "+ child +"</li>"
				else:
					response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a>"+ child +"</li>"					
		if len(response):
			response = "<ul>" + response + "</ul>"
		return response