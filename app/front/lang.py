# -*- coding: utf-8 -*-

class Lang(object):
	
################################ INICIO - Español ################################

	def inicio(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Bienvenidos a Garita Otay',
				'menu_inicio': 'current',
				'section': 'inicio',
				'section_lang': 'home',
			},
			'submenu': {
				'id': 'm_inicio_layer',
				'a': 'Su Mejor Alternativa',
				'b': 'en <strong>Trámites y Permisos</strong>',
			},
			'a': {
				'title': 'Servicios',
				'desc': 'Servicios Garita Otay ofrece soluciones al sector transportista tanto público como privado en lo que respecta a seguros, consultoría y permisos de transporte de carga.'
			},
			'tramites':{
				'title': 'Trámites',
				'href': 'tramites',
				'desc': 'Nos encargamos de gestionar y tramitar sus registros necesarios para cumplir con los reglamentos requeridos. ',
				'btn_text': 'ver más',
				'btn_href': 'tramites',
			},
			'permisos':{
				'title': 'Permisos',
				'href': 'permisos',
				'desc': 'En Servicios Garita Otay nos distinguimos por brindar a nuestros clientes seguridad. <br> <br>Somos agentes directos y autorizados por la Comisión Nacional de Seguros y Fianzas de México.',
				'btn_text': 'ver más',
				'btn_href': 'permisos',
			},
			'seguros':{
				'title': 'Seguros',
				'href': 'seguros',
				'desc': 'Le brindamos apoyo profesional ante los diversos formatos requeridos por dependencias de gobierno.',
				'btn_text': 'ver más',
				'btn_href': 'seguros',
			},
			'auditorias':{
				'title': 'Auditorías',
				'href': 'auditorias',
				'desc': 'Usted evitará largas filas, trámites complicados y sólo obtendrá la satisfacción de contar con su movimiento a tiempo.',
				'btn_text': 'ver más',
				'btn_href': 'auditorias',
			},
			'nosotros': {
				'title': 'Nosotros',
				'desc': 'Con más de 20 años de trabajo, Servicios Garita Otay ha logrado satisfacer las necesidades de sus clientes y superar sus expectativas.',
				'btn_text': 'conócenos',
				'btn_href': 'nosotros',
			},
			'contacto': {
				'btn_text': 'Contáctenos',
				'btn_href': 'contacto',
			},
			'compra_linea': {
				'title': 'Compra en Línea',
				'desc': '<p>Evite ser multado, que su vehículo sea remolcado y evite contratiempos en la línea.</p> <h3>¡Adquiera su seguro de vehículo hoy mismo!</h3>',
				'btn_text': 'Compra en Línea',
				'btn_href': 'compra_linea',	
			}
		}
		return data


################################ INICIO - English ################################

	def home(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Welcome to Garita Otay',
				'menu_inicio': 'current',
				'section': 'inicio',
				'section_lang': 'home',				
			},
			'submenu': {
				'id': 'm_home_layer',
				'a': 'Your best alternative',
				'b': 'in <strong>Procedures and Permits</span>',
			},
			'a': {
				'title': 'Services',
				'desc': 'Servicios Garita Otay offers insurance, consulting and freight transport permits solutions to the transportation sector, both public and private.'
			},
			'quienes_somos': {
				'title': 'Services',
				'desc': 'Servicios Garita Otay ofrece soluciones al sector transportista tanto público como privado en lo que respecta a seguros, consultoría y permisos de transporte de carga.'
			},
			'tramites':{
				'title': 'Procedures',
				'href': 'procedures',
				'desc': '<strong>Servicios Garita Otay</strong> takes charge in a timely manner, efficiently managing your required records in order to comply with regulations. Most of these permits are through the International Freight Transport in California and Baja California.',
				'btn_text': 'read more',
				'btn_href': 'procedures',
			},
			'permisos':{
				'title': 'Permits',
				'href': 'permits',
				'desc': 'There are several permits and records, among other files, that require frequent updating in order to comply with statutes and regulations in different sectors, such as the United States Department of Transportion and the Department of Motor Vehicles in the U.S.',
				'btn_text': 'read more',
				'btn_href': 'permits',
			},
			'seguros':{
				'title': 'Insurance',
				'href': 'insurance',
				'desc': 'Our Insurance Department provides our clients with security and protection from diverse risks, such as health, residential home, medical bills, life insurance, auto and transportation amongst others',
				'btn_text': 'read more',
				'btn_href': 'insurance',
			},
			'auditorias':{
				'title': 'Consultation and<br /> Audit Department',
				'href': 'audits',
				'desc': 'We offer you professional support in diverse formats from different government agencies. Our company provides consultation, especially to companies dedicated to public and private transportation of international freight.',
				'btn_text': 'read more',
				'btn_href': 'audits',
			},
			'nosotros': {
				'title': 'About us',
				'desc': 'With more than 20 years of service, Servicios Garita Otay has met its client’s needs and exceeded their expectations',
				'btn_text': 'read more',
				'btn_href': 'about-us',
			},
			'contacto': {
				'btn_text': 'Contact us',
				'btn_href': 'Contact us',
			},
			'compra_linea': {
				'title': 'Buy Online',
				'desc': '<p>Avoid being fined, your vehicle being towed or any hassles on your border crossing.</p> <h3>Get your auto insurance today!</h3>',
				'btn_text': 'Buy Online',
				'btn_href': 'buy_online',	
			}
		}
		return data


################################ NOSOTROS - Español ################################

	def nosotros(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Nosotros',
				'menu_inicio': 'current',
				'section': 'nosotros',
				'section_lang': 'about-us',				
			},
			'submenu':{
				'id': 'm_nosotros_layer',
				'title': 'Nosotros',
				'href': 'nosotros',
				'list': [
					{
						'href': 'quienes-somos',
						'title': 'Quiénes somos'
					},
					{
						'href': 'mision-vision',
						'title': 'Misión y Visión'
					},
					{
						'href': 'valores',
						'title': 'Valores'
					},
					{
						'href': 'ventajas-competitivas',
						'title': 'Ventajas Competitivas',
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
			'services': {
				'title': '¿Quiénes somos?',
				'desc': '<p>SERVICIOS GARITA OTAY es una empresa consolidada y líder en la industria; se fundó en 1990. La empresa de servicios ofrece soluciones al sector transportista tanto público como privado  en lo que respecta a seguros, consultoría y permisos de transporte de carga. Con más de 20 años de trabajo, Servicios Garita Otay ha logrado satisfacer las necesidades de sus clientes y superar sus expectativas.</p><p>La empresa cuenta con personal altamente calificado y especializado en el giro, que además tiene amplio conocimiento de la operación y mantiene excelente relación con dependencias gubernamentales en ambos lados de la frontera que son las responsables de emitir permisos y licencias para el transporte de carga. La atención a los clientes se ofrece en inglés y en español. </p><p>La compañía se adhiere a las normas de los organismos reguladores de transporte tanto en México como en Estados Unidos y está acreditada con las licencias correspondientes para su operación, emitidas por la Comisión Nacional  de Seguros y Fianzas de México y por el Departamento de Seguros de California (California Department of Insurance).  </p>',
				'recognition':'El trabajo de Servicios Garita Otay se ha visto reconocido al hacerse acreedor de los siguientes premios: Premios Diamante 2010, 2011, 2012 Compañía CAIC.',
				'prize':'Premio Diamante',
			
			},
			'mission':{
				'title': 'Misión',
				'desc': 'Nuestra misión en Servicios Garita Otay es garantizar y comprometernos a ofrecer servicio de calidad y atención personalizada a cada uno de nuestros clientes mediante la gestión de una amplia gama de productos y servicios que ofrezcan una solución para todas sus necesidades de transporte en carreteras a lo largo de Estados Unidos y México. ',
			},
			'vision':{
				'title': 'Visión',
				'desc': 'Nuestra visión en Servicios Garita Otay es mantener el liderazgo dentro de la industria mediante la prestación de servicios y realización de trámites de forma puntual y personalizada al mejor precio, que nos permitan mantener un enlace y relación duradera con nuestros clientes.',
			},
			'values':{
				'title': 'Valores',
				'desc': 'Servicios Garita Otay tiene como valores la calidad humana, ética, honestidad, responsabilidad y compromiso con nuestros clientes. Es de suma importancia brindar a nuestros colaboradores y clientes la mayor satisfacción y calidad en nuestro trabajo.',
			},
			'values_list':{
				'ethic_title': 'Ética profesional',
				'ethic_desc': 'En cada proyecto es nuestro compromiso respetar la confianza que nuestro cliente deposita en nosotros.',
				'honesty_title': 'Honestidad',
				'honesty_desc': 'Es fundamental para nosotros que la información proporcionada a nuestros clientes sea con total honestidad, basada en hechos firmes y verídicos.',
				'commitment_title': 'Compromiso',
				'commitment_desc': 'El enlace que existe entre nuestros clientes y colaboradores es de suma importancia para mantener un proyecto asignado con calidad y satisfacción.',
				'human_quality_title': 'Calidad humana',
				'human_quality_desc': 'Nuestra calidez humana es fundamental y se manifiesta en la atención personalizada, el interés y la sencillez que mostramos ante nuestros clientes, lo que permite un entorno de armonía y trabajo constante.',
			},
			'competitive_advantage': {
				'title': 'Ventajas Competitivas',
				'desc': 'La experiencia y el compromiso de Garita Otay le han permitido acumular ventajas competitivas que la mantienen en el liderazgo de la industria, por ejemplo, entre lo más sobresaliente está:',
				'list_left':"<li>Atención personalizada</li><li>20 años de experiencia y operación en el mercado de Estados Unidos y México</li><li>Especialistas y expertos en seguros comerciales, particulares, permisos y trámites para transporte público y privado</li><li>Agente directo profesional de seguros con certificación ante la Comisión Nacional de Seguros y Fianzas de México y el Departamento de Seguros de California</li><li>Atención, tramitación y consultoría 100% bilingüe</li>",
				'list_right':"<li>Puntualidad  y celeridad en los procesos y trámites</li><li>Oficinas establecidas tanto en México como en Estados Unidos (Otay Mesa, California)</li><li>Horarios amplios para conveniencia del cliente</li><li>Verificaciones certificadas por el DMV</li><li>Financiamiento para clientes</li>",
			},
			'our_clients':{
				'title':'Nuestros Clientes',
				'subtitle':'Otros Clientes',
				'l1':'DCA Transportes de Mexico',
				'l2':'TILI Logistics Corporation',
				'l3':'Correcaminos',
				'l4':'Los Pinos',
				'l5':'Transportes Santa Monica',
				'l6':'Transportes Don Juanito',
			},
			'insurance_companies':{
				'title': 'Compañías de Seguros que Representamos',
				'comp_ame': 'Compañías de Seguros Americanas',
				'comp_mex': 'Compañías de Seguros Mexicanas',
			}
		}
		return data

################################ NOSOTROS - English ################################

	def about_us(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'About us',
				'menu_inicio': 'current',
				'section': 'nosotros',
				'section_lang': 'about-us',				
			},
			'submenu':{	
				'id': 'm_about-us_layer',	
				'title': 'About Us',
				'href': 'about-us',
				'list': 
					[
						{
							'href': 'who-are-we',
							'title': 'Who are we',
						},
						{
							'href': 'mission-vision',
							'title': 'Mission and Vision',
						},
						{
							'href': 'values',
							'title': 'Values',
						},
						{
							'href': 'competitive-advantages',
							'title': 'Competitive advantages',
						},
						{
							'href': 'our-clients',
							'title': 'Our clients',
						},
						{
							'href': 'insurance-companies',
							'title': 'Insurance Companies we Represent',
						},
					]
			},
			'services': {
				'title': 'About Us',
				'desc': '<p>SERVICIOS GARITA OTAY is an established company leader in its industry, founded in 1990. This company offers solutions to the transportation sector, both public as well as private. With more than 20 years of service, Servicios Garita Otay has met its client’s needs and exceeded their expectations.</p><p>The company has highly qualified and specialized personnel with broad knowledge of their company operations and an excellent relationship with government agencies on both sides of the border that are responsible for issuing permits and licenses for freight transportation. Clients are assisted in both English and Spanish.</p><p>Servicios Garita Otay complies with Mexican and American transport regulations, and is credited with the adequate operating license, issued by the National Commission of Insurance and Bonding in Mexico (CNFS, for its acronym in English) and by the California Department of Insurance.</p>',
				'recognition':'The work of Servicios Garita Otay has been recognized with the following awards: Diamond Award 2010, 2011, 2012 by CAIC.',
				'prize':'Diamond Prize',

			},
			'mission':{
				'title': 'Mission',
				'desc': 'Our mission at Servicios Garita Otay is a guarantee and commitment to providing high quality service and personalized assistance to each one of our clients. This promise is through the proper management of a wide range of products and services that will translate into a solution for our client’s needs of road transportation along the United States and Mexico. ',
			},
			'vision':{
				'title': 'Vision',
				'desc': 'Our vision at Servicios Garita Otay is to maintain leadership within our industry by providing quality service and client processing in a timely and customized manner. We also offer the best rates available in order to sustain a bond and a long lasting relationship with our clients.',
			},
			'values':{
				'title': 'Values',
				'desc': 'Our company carries core values such as human quality, ethics, honesty, and responsibility and commitment to our clients. It is essential to deliver the highest satisfaction and quality in our work towards our collaborators and clients.',
			},
			'values_list':{
				'ethic_title': 'Professional ethics',
				'ethic_desc': 'In each one of our projects, it is our commitment to respect the trust and confidence that our client has placed in us.',
				'honesty_title': 'Honesty',
				'honesty_desc': 'It is fundamental to us that the information provided to our clients is based on complete honesty, firm and true facts.',
				'commitment_title': 'Commitment',
				'commitment_desc': 'The bond between our clients and collaborators is very important in managing an assigned project with quality and meeting their expectations.',
				'human_quality_title': 'Customer relations',
				'human_quality_desc': 'Our customer relations are essential and it is reflected in our personalized service, our interest and humble attitude shown before our clients, allowing us to work in an environment of compatibility and consistency.',
			},
			'competitive_advantage': {
				'title': 'Competitive advantages',
				'desc': 'Experience and commitment has allowed the company to accumulate a substantial competitive advantage that allows market leadership. For example, among the most outstanding are:',
				'list_left':"<li>Customized assistance</li><li>20-year experience and operation in the North American and Mexican markets.</li><li>Specialized experts in commercial and private insurance; permits and processes for public and private transport.</li><li>Professional and independent insurance agent with certification by the National Commission of Insurance and Bonds in Mexico and by the California Department of Insurance.</li><li>100% bilingual assistance, consulting and processing.</li>",
				'list_right':"<li>Punctuality and clarity in processing paperwork.</li><li>Office facilities in Mexico and the United States (Otay Mesa, CA).</li><li>Convenient office hours.</li><li>Certified verifications by the DMV.</li><li>Client financing available.</li>",
			},
			'our_clients':{
				'title': 'Our Clients',
				'subtitle': 'Other Clients',
				'l1':'DCA Transportes de Mexico',
				'l2':'TILI Logistics Corporation',
				'l3':'Correcaminos',
				'l4':'Los Pinos',
				'l5':'Transportes Santa Monica',
				'l6':'Transportes Don Juanito'
			},
			'insurance_companies':{
				'title': 'Insurance Companies we Represent',
				'comp_ame': 'American Insurance Companies',
				'comp_mex': 'Mexican Insurance Companies',
			}
		}
		return data
		
################################ TRAMITES Y PERMISOS - Español ################################


	def tramites_permisos(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Tramites',
				'menu_inicio': 'current',
				'section': 'tramites',
				'section_lang': 'procedures',			
			},
			'submenu': {
				'title': 'Trámites y Permisos',
				'href': 'tramites',
				'list_a': {
					'title': 'Trámites',
					'href': 'tramites',
					'items': [
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
					],
				},
				'list_b': {
					'title': 'Permisos',
					'href': 'permisos',
					'items': [
						{
							'href': 'eu',
							'title': 'Permisos en E.U.',
						},						
					],
				}
			},
			'tramites_permisos': {
				'title': 'Trámites',
				'button_text': 'Ir a permisos',
				'button_url': 'permisos',
				'desc_left': 'Existen diversos permisos y registros, entre otros procesos, que deben actualizarse con cierta frecuencia para cumplir con las normas y regulaciones ante diferentes sectores, por ejemplo, el Departamento de Transporte de Estados Unidos (DOT), el Departamento de Vehículos Motorizados de California (DMV) y, en México, la Secretaría de Comunicaciones y Transportes (SCT), entre otras.',
				'desc_right': '<strong>Servicios Garita Otay</strong> oportunamente se encarga de gestionar y tramitar sus registros  necesarios para cumplir con los reglamentos requeridos. La mayoría de estos permisos son a través de Transporte de Carga Internacional en ambas Californias.'
			},
			'dmv':{
				'title': 'Trámites DMV',
				'subtitle': 'Conoce nuestros trámites DMV',
			},			
			'eu': {
				'title': 'Trámites en E.U.',
				'subtitle': 'Conoce nuestros trámites en E.U.',				
			},
			'mx': {
				'title': 'Trámites en México',
				'subtitle': 'Conoce nuestros trámites en México',					
			},
		}
		return data

################################ TRAMITES Y PERMISOS - English ################################

	def procedures(self):
		data = {
		'info_gral': { 
			'page_title': 'Garita Otay',
			'keywors': 'Garita Otay',
			'description': 'Tramites',
			'menu_inicio': 'current',
			'section': 'tramites',
			'section_lang': 'procedures',			
		},
		'submenu': {
			'title': 'Procedures and permits',
			'href': 'tramits',
			'list_a': {
				'title': 'Procedures',
				'href': 'procedures',
				'items': [
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
				],
			},
			'list_b': {
				'title': 'Permits',
				'href': 'permits',
				'items': [
					{
						'href': 'us',
						'title': 'Permits in U.S.',
					},						
				],
			}
		},
		'tramites_permisos': {
			'title': 'Procedures',
			'button_text': 'Go to permits',
			'button_url': 'permits',
			'desc_left': 'There are several permits and records, among other files, that require frequent updating in order to comply with statutes and regulations in different sectors, such as the Department of Transport and the Department of Motor Vehicles in the U.S., and the Mexican Secretariat of Communications and Transport, among others.',
			'desc_right': '<strong>Servicios Garita Otay</strong> takes charge in a timely manner, efficiently managing your required records in order to comply with regulations. Most of these permits are through the International Freight Transport in California and Baja California.',
		},
		'dmv': {
			'title': 'DMV paperwork',
			'subtitle': 'Meet our DMV procedures',
		},
		'eu': {
			'title': 'PROCEEDINGS IN THE U.S.',
			'subtitle': 'Meet our procedures in E.U.',
		},
			'mx': {
				'title': 'PROCEEDINGS IN MEXICO',
				'subtitle': 'Meet our procedures in Mexico',
			},
		}
		return data

################################ PERMISOS - Español ################################


	def permisos(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Permisos',
				'section': 'permisos',
				'section_lang': 'permits',			
			},
			'submenu': {
				'title': 'Permisos',
				'href': 'tramites',
				'list_a': {
					'title': 'Trámites',
					'href': 'tramites',
					'items': [
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
					],
				},
				'list_b': {
					'title': 'Permisos',
					'href': 'permisos',
					'items': [
						{
							'href': 'eu',
							'title': 'Permisos en E.U.',
						},						
					],
				}
			},
			'tramites_permisos': {
				'title': 'Permisos',
				'subtitle': 'Permisos en E.U.',
				'button_text': 'Ir a trámites',
				'button_url': 'tramites',
				'desc_left': 'Existen diversos permisos y registros, entre otros procesos, que deben actualizarse con cierta frecuencia para cumplir con las normas y regulaciones ante diferentes sectores, por ejemplo, el Departamento de Transporte de Estados Unidos (DOT), el Departamento de Vehículos Motorizados de California (DMV) y, en México, la Secretaría de Comunicaciones y Transportes (SCT), entre otras.',
				'desc_right': '<strong>Servicios Garita Otay</strong> oportunamente se encarga de gestionar y tramitar sus registros  necesarios para cumplir con los reglamentos requeridos. La mayoría de estos permisos son a través de Transporte de Carga Internacional en ambas Californias.'
			},
		}
		return data

################################ PERMITS - English ################################



	def permits(self):
		data = {
			'info_gral': { 
				'page_title': 'ENGLISH-Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Tramites',
				'section': 'permisos',
				'section_lang': 'permits',			
			},
			'submenu': {
			'title': 'Procedures and Permits',
			'href': 'procedures',
			'list_a': {
				'title': 'Procedures',
				'href': 'procedures',
				'items': [
					{
						'href': 'dmv',
						'title': 'Procedures DMV',
					},
					{
						'href': 'eu',
						'title': 'Procedures in U.S.',
					},
					{
						'href': 'mexico',
						'title': 'Procedures in Mexico',
					},
				],
			},
			'list_b': {
				'title': 'Permits',
				'href': 'permits',
				'items': [
					{
						'href': 'eu',
						'title': 'Permits in U.S.',
					},						
				],
			}
		},
			'tramites_permisos': {
				'title': 'Permits',
				'subtitle': 'U.S. PERMITS',
				'button_text': 'Go to procedures',
				'button_url': 'procedures',
				'desc_left': 'There are several permits and records, among other files, that require frequent updating in order to comply with statutes and regulations in different sectors, such as the Department of Transport and the Department of Motor Vehicles in the U.S., and the Mexican Secretariat of Communications and Transport, among others.',
				'desc_right': '<strong>Servicios Garita Otay</strong> takes charge in a timely manner, efficiently managing your required records in order to comply with regulations. Most of these permits are through the International Freight Transport in California and Baja California.',
			}
		}
		return data

################################ SEGUROS - Español ################################

	def seguros(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Seguros',
				'menu_inicio': 'current',
				'section': 'seguros',
				'section_lang': 'insurance',			
			},
			'submenu': {
				'title': 'Seguros',
				'href': 'seguros',
				'list': [
					{
						'title': 'Seguros en E.U.',
						'href': 'eu',
					},
					{
						'title': 'Seguros en México',
						'href': 'mexico',
					},
				]
			},
			'eu': {
				'title': 'Seguros en E.U.',
				'subtitle': 'Conoce nuestros seguros en E.U.',
			},			
			'mx': {
				'title': 'Seguros en México',
				'subtitle': 'Conoce nuestros seguros en México',
			},
		}
		return data

################################ INSURANCE - English ################################

	def insurance(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Seguros',
				'menu_inicio': 'current',
				'section': 'seguros',
				'section_lang': 'insurance',			
			},
			'submenu': {
				'title': 'Insurance',
				'href': 'insurance',
				'list': [
					{
						'title': 'Insurance in U.S.',
						'href': 'us',
					},
					{
						'title': 'Insurance in Mexico',
						'href': 'mexico',
					},
				]
			},
			'eu': {
				'title': 'INSURANCE IN THE U.S.',
				'subtitle': 'Meet our E.U. insurance',
			},			
			'mx': {
				'title': 'INSURANCE IN MEXICO',
				'subtitle': 'Meet our insurance in Mexico',
			},
		}
		return data

################################ AUDITORIAS - Español ################################

	def auditorias(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'auditorias',
				'section': 'auditorias',
				'section_lang': 'audits',
				'title': 'Auditorías',
				'subtitle': 'Servicio de consultoría en auditorías'
			},
			'submenu': {
				'title': 'Auditorías',
				'subtitle': 'Servicio de consultoría en auditorías',
			},
			'departamento': {
				'title': 'Departamento de Consultoría <br />y Asesoría',
				'desc': '<p><strong>Servicios Garita Otay</strong> le brinda apoyo profesional ante los diversos formatos requeridos por dependencias de gobierno. Asesoramos y damos consultoría principalmente a aquellas compañías que se dedican al transporte público y privado de carga internacional.</p><p>La experiencia y capacidad del personal que lo asiste permite en la mayoría de las inspecciones y auditorías federales o estatales lograr satisfacción y mejoría integral en el proceso de documentación necesario para cumplir con las reglas de las dependencias gubernamentales, como el Departamento de Transporte (DOT), California Highway Patrol, State Board of Equalization DIESEL, IFTA, Air Resource Board, ARB, Internal Revenue Service y IRS, entre otras.</p>',
				'alt': 'Te asesoramos en tus auditorías',
				'list': {
					'a' : 'Asesoría para elaborar expediente de chofer',
					'b' : 'Asesoría para elaborar expediente de chofer',
					'c' : 'Asesoría pre-auditoría DOT, CHP',
					'd' : 'Auditorías DOT, CHP',
					'e' : 'Auditorías BIT',
					'f' : 'Asesoría ante el State Board of Equalization',
				}
			},
		}
		return data

################################ AUDITS - ENGLISH ################################

	def audits(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'auditorias',
				'section': 'auditorias',
				'section_lang': 'audits',
				'title': 'Audits',
				'subtitle': 'Consultation and Audit Department'
			},
			'submenu': {
				'title': 'Audits',
				'subtitle': 'Consultory service in audits',
			},
			'departamento': {
				'title': 'Consultation and Audit Department',
				'desc': '<p><strong>Servicios Garita Otay</strong> offers you professional support in diverse formats from different government agencies. Our company provides consultation, especially to companies dedicated to public and private transportation of international freight.</p><p>The experience and assistance that our staff will provide for your company’s federal and state inspections and audits will meet your expectations and contribute to a comprehensive improvement of your documentation process. This process shall allow you to comply with various governmental regulations such as the Department of Transportation, the California Highway Patrol, the State Board of Equalization DIESEL, IFTA, the Air Resource Board, ARB, and the Internal Revenue Service, amongst other.</p>',
				'alt': 'Te asesoramos en tus auditorías',
				'list': {
					'a': 'Counseling to create a driver file',
					'b': 'Logbook revision',
					'c': 'DOT, CHP pre-audit consultation',
					'd': 'DOT, CHP audits',
					'e': 'BIT audits',
					'f': 'Consultation before the State Board of Equalization',
				}
			},
		}
		return data

################################ COMPRA EN LINEA - Español ################################

	def compra_linea(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Compra en línea',
				'section': 'compra_linea',
				'section_lang': 'buy_online',
				'title': 'Compra en Línea',
			},
			'submenu': {
				'title': 'Compra en línea',
			},
			'section':{
				'intro': 'Bienvenidos al portal en línea de <strong>Servicios Garita Otay</strong>.',
				'desc': '<p>Usted encontrará la información necesaria para comprar una póliza de seguro de manera fácil y rápida. </p><p>	Evite ser multado, que su vehículo sea remolcado y evite contratiempos en la línea.</p>',
				'foot': '¡Adquiera su seguro de vehículo hoy mismo!',
				'alt': 'Haz tus compras en línea',
				'header_insurance': 'Seguro de auto no residente.',
				'insurance_text': 'Seguro de responsablidad civil automovilista para vehículos particulares registrados en México que entrarán a Estados Unidos de manera OCASIONAL',
				'insurance_link': 'http://emision.safeins.com/portal/inter-red',
				'insurance_title': 'Comprar seguro de auto no residente',
				'insurance_link_text': 'Comprar',
			}
		}
		return data

################################ BUY ONLINE - ENGLISH ################################

	def buy_online(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Buy online',
				'section': 'compra_linea',
				'section_lang': 'buy_online',
				'title': 'Buy online',
			},
			'submenu': {
				'title': 'Buy online',
			},
			'section':{
				'intro': 'Welcome to the <strong>Servicios Garita Otay</strong> online portal!',
				'desc': '<p>Here you will find all the necessary information to simply and efficiently purchase an insurance policy.</p><p>Avoid being fined, your vehicle being towed or any hassles on your border crossing.</p>',
				'foot': 'Get your auto insurance today!',
				'alt': 'Get your auto insurance today!',
				'header_insurance': 'Nonresident auto insurance',
				'insurance_text': 'Civil Liability Insurance motorist for cars registered in Mexico to enter the United States on a CASUAL',
				'insurance_link': 'http://emision.safeins.com/portal/inter-red',
				'insurance_title': 'Get your nonresident auto insurance',
				'insurance_link_text': 'Buy',
			}
		}
		return data

################################ CONTACTO - Español ################################

	def contacto(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Compra en línea',
				'section': 'contacto',
				'section_lang': 'contact',
				'title': 'Contacto',
			},
			'submenu': {
				'title': 'Contacto',
			},
			'gral':{
				'title': 'Contacto general',
				'mx_country': 'México',
				'mx_city': 'Tijuana',
				'mx_address': 'Blvd. 3a Oeste 17601-104, Garita de Otay<br />Tijuana, BC. MX',
				'mx_tel_a': '011 52 (664) 623 7742',	
				'mx_tel_b': '011 52 (664) 623 7743',
				'mx_fax': '011 52 (664) 647 5509',
				'eu_country': 'E.U.',
				'eu_city': 'San Diego',
				'eu_address': '9765  Marconi  Dr. 105<br />San Diego, CA 92154, USA',
				'eu_tel': '(619) 710 0451',
				'eu_fax': '(619) 710 4827',
			},
			'form': {
				'title': 'Forma de contacto',
				'subtitle': 'Para solicitud de información u otros mensajes, por favor utilice la siguiente forma. Haremos todo lo posible para responder a la mayor brevedad ¡Gracias!',
				'name': 'Nombre / Empresa',
				'email': 'E-mail',
				'telephone': 'Teléfono',
				'services': 'Servicio de interés',
				'message': 'Mensaje',
				'help': 'Campos Obligatorios',
				'send': 'Enviar',
				'list_services':'<option>Trámites DMV</option><option>Trámites E.U.</option><option>Trámites México</option><option>Permisos E.U.</option><option>Seguros E.U. </option><option>Seguros México</option><option>Auditorías</option><option>Otro</option>',
			},
			'directory': {
				'title': 'Directorio',
				'contact': 'Contacta a',
				'employees': [
					{
						'name': 'Sra. Rosario Isabel Rojo ',
						'mail': 'isabel@serviciosgaritaotay.com',
						'position': 'Administración General',
						'radio': 'ID 44*990444*1',
					},
					{
						'name': 'Ing. Mario Hernández',
						'mail': 'mario@serviciosgaritaotay.com',
						'position': 'Departamento de Permisos y Trámites ',
						'radio': '44*990444*2',
					},
					{
						'name': 'Manuel Hernández',
						'mail': 'manuel@serviciosgaritaotay.com',
						'position': 'Departamento de Seguros E.U. - Comerciales',
					},
					{
						'name': 'L.N.I. Karla Suffo ',
						'mail': 'karla@serviciosgaritaotay.com',
						'position': 'Departamento de Seguros E.U. - Comerciales',
						'radio': '122*717583*3',
					},
					{
						'name': 'Lic. Deisy Merchant Pérez',
						'mail': 'deisy@serviciosgaritaotay.com',
						'position': 'Departamento de Seguros Mexicanos, Permisos Mexicanos y Americanos',
						'radio': '44*990444*3',
					},
					{
						'name': 'Sergio Pasten',
						'mail': 'sergio@serviciosgaritaotay.com',
						'position': 'Departamento de Registro y Placas',
						'radio': '44*990444*1',
					},
					{
						'name': 'Lic. Johanna Cisneros Flores',
						'mail': 'johanna@serviciosgaritaotay.com',
						'position': 'Departamento de Placas,  Crédito y Cobranza',
						'radio': '44*990444*3',
					},
				]
			}
		}
		return data

################################ BUY ONLINE - ENGLISH ################################

	def contact(self):
		data = {
			'info_gral': { 
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Compra en línea',
				'section': 'contacto',
				'section_lang': 'contact',
				'title': 'Contact',
			},
			'submenu': {
				'title': 'Contact',
			},
			'gral':{
				'title': 'Contact',
				'mx_country': 'México',
				'mx_city': 'Tijuana',
				'mx_address': 'Blvd. 3a Oeste 17601-104, Garita de Otay<br />Tijuana, BC. MX',
				'mx_tel_a': '011 52 (664) 623 7742',	
				'mx_tel_b': '011 52 (664) 623 7743',
				'mx_fax': '011 52 (664) 647 5509',
				'eu_country': 'E.U.',
				'eu_city': 'San Diego',
				'eu_address': '9765  Marconi  Dr. 105<br />San Diego, CA 92154, USA',
				'eu_tel': '(619) 710 0451',
				'eu_fax': '(619) 710 4827',
			},
			'form': {
				'title': 'Contact form',
				'subtitle': 'To request information or other messages, please use the following form. We will endeavor to respond as soon as possible Thanks!',
				'name': 'Name / Company',
				'email': 'E-mail',
				'telephone': 'Telephone',
				'services': 'Services',
				'message': 'Message',
				'help': 'Required fields',
				'send': 'Send',
				'list_services':'<option>DMV paperwork</option><option>Proceedings in the U.S.</option><option>Proceedings in Mexico</option><option>U.S. Permits</option><option>Insurance in the U.S. </option><option>Insurance in Mexico</option><option>Audits</option><option>Other</option>',
			},
			'directory': {
				'title': 'Directory',
				'contact': 'Contact to',
				'employees': [
					{
						'name': 'Mrs. Rosario Isabel Rojo ',
						'mail': 'isabel@serviciosgaritaotay.com',
						'position': 'General Administration',
						'radio': 'ID 125*120*3687',
					},
					{
						'name': 'Ing. Mario Hernández',
						'mail': 'mario@serviciosgaritaotay.com',
						'position': 'Department of Permits and Procedures',
						'radio': '44*990444*2',
					},
					{
						'name': 'Manuel Hernández',
						'mail': 'manuel@serviciosgaritaotay.com',
						'position': 'E.U. Insurance Department - Commercial',
					},
					{
						'name': 'L.N.I. Karla Suffo ',
						'mail': 'karla@serviciosgaritaotay.com',
						'position': 'E.U. Insurance Department - Commercial',
						'radio': '44*990444*1',
					},
					{
						'name': 'Lic. Deisy Merchant Pérez',
						'mail': 'deisy@serviciosgaritaotay.com',
						'position': 'Mexican Insurance Department, Mexican and American Permissions',
						'radio': '44*990444*3',
					},
					{
						'name': 'Sergio Pasten',
						'mail': 'sergio@serviciosgaritaotay.com',
						'position': 'Department of Registration and Plates',
						'radio': '44*990444*1',
					},
					{
						'name': 'Johanna Cisneros Flores',
						'mail': 'johanna@serviciosgaritaotay.com',
						'position': 'Plate Department, Credit and Collections',
						'radio': '44*990444*3',
					},
				]
			}
		}
		return data