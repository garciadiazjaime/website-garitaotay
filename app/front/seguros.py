# -*- coding: utf-8 -*-

class Seguros(object):
	
	def eu(self, lang=0):
		data = [
			[
				{
					'id': 'eu_default',
					'desc': '<p>En el Departamento de <strong>Seguros en Servicios Garita Otay</strong> nos distinguimos por brindar a nuestros clientes seguridad y protección en diversos riesgos, como salud, casa-habitación, gastos médicos, de vida, de autos y transportes, entre otros.</p><p>Las coberturas de responsabilidad civil para unidades de carga se establecen por ley en Estados Unidos y están reguladas por el FMCSA – DOT, exclusivamente para autoridades MX, MC, DOT, CA. </p><p>Los límites pueden ser variables, desde 15 millas zona comercial hasta cobertura en los 48 estados de la Unión Norteamericana.</p>',
				},
				{
					'id': 'eu_responsabilidad_civil',
					'title': 'Pólizas de Responsabilidad Civil en E.U. - Autos y Camiones ',
					'desc': 'Cobertura de responsabilidad civil por daños a terceros: Antes de cruzar la frontera es obligatorio contar con una póliza de seguro con los  términos  requeridos por el Departamento de Seguros de California.',
				},
				{
					'id': 'eu_danos_fisicos',
					'title': 'Daños Físicos en la Propiedad en Autos y Camiones',
					'desc': 'Llámese cobertura amplia para amparar la pérdida parcial o total de un bien asegurado, contratado en una póliza de cobertura total.',
				},
				{
					'id': 'eu_compensacion_laboral',
					'title': 'Compensación laboral',
					'desc': 'Cobertura para choferes, en caso de sufrir un accidente o eventualidad  dentro del trabajo. La compañía de seguros está obligada a cubrir los gastos médicos, incluso hasta indemnizar a la persona. ',
				},
				{
					'id': 'eu_cargo_mercancias',
					'title': 'Seguro de Cargo, Mercancías',
					'desc': 'Cobertura de mercancías. La compañía de seguros se obliga a pagar la suma contratada en caso de accidente o pérdida total de la mercancía transportada (mercancía en general, perecederos, electrónicos, etc.)',
				},
				{
					'id': 'eu_responsabilidad_general',
					'title': 'Responsabilidad General ',
					'desc': 'Es la responsabilidad del transportista que aplica cuando el chofer no está al volante.',
				},
				{
					'id': 'eu_poliza_auto',
					'title': 'Póliza de Auto (Particular, Placas Fronterizas, Nacionales, Norteamericanas)',
					'desc': 'El contrato de una póliza de responsabilidad civil garantiza la cobertura y el daño reparado a bienes en un evento ocasionado por un siniestro en carreteras de Estados Unidos.',
				},
				{
					'id': 'eu_responsabilidad_general_trailer',
					'title': 'Responsabilidad General - Seguro para Tráiler-Remolque No Identificado',
					'desc': 'Cobertura para caja o plataforma: En caso que el equipo movido no sea de su propietario y que el legítimo dueño sea un tercero, la compañía de seguros  está  obligada a cubrir en su totalidad  la pérdida parcial o total de la propiedad.',
				},			
				{
					'id': 'eu_poliza_exceso',
					'title': 'Póliza de Exceso  ',
					'desc': 'Es una póliza de cobertura adicional individual de gastos médicos mayores u otro tipo de riesgo. Normalmente opera sobre la base de la contratación previa de una póliza primaria, con una suma asegurada que permite atender los gastos que no sean cubiertos por dicha póliza primaria.',
				},
				{				
					'id': 'eu_seguro_traslado',
					'title': 'Seguros de Traslado por Días (1, 3 y 7 días) en Estados Unidos',
					'desc': 'Cobertura de responsabilidad civil por viaje contratada por camiones que viajan partiendo de un punto a un destino final. En su caso son unidades que no cuentan con permisos comerciales y la mayoría no tienen registro de placas ante el DMV. Se amparan con documentos de la propiedad y el seguro.',
				},		
			],
			[
				{
					'id': 'eu_default',
					'desc': '<p>The outstanding work we do at <strong>Seguros en Servicios Garita Otay</strong> through our Insurance Department provides our clients with security and protection from diverse risks, such as health, residential home, medical bills, life insurance, auto and transportation amongst others.</p><p>Coverage for civil liability for freight units is established by law in the U.S., and is regulated by <b>FMCSA – DOT</b>, exclusively for <b>MX</b>, <b>MC</b>, <b>DOT</b>, and <b>CA</b> authorities.</p><p>Limits may vary from 15 miles of commercial zone to coverage of the 48 states in North America.</p>',
				},
				{
					'id': 'eu_responsabilidad_civil',
					'title': 'Civil Liability Policies in the U. S. – Auto and Trucks',
					'desc': 'Civil liability coverage covers damage to third parties. Before crossing the border, it is mandatory to have an insurance policy with the requirements established by the California Insurance Department.',
				},
				{
					'id': 'eu_danos_fisicos',
					'title': 'Physical Damage to Autos and Trucks',
					'desc': 'Full coverage to bear the total loss or partial loss of the insured asset.',
				},
				{
					'id': 'eu_compensacion_laboral',
					'title': 'Worker’s Compensation',
					'desc': 'Worker’s Compensation provides coverage for drivers in the case of a work- related accident or contingency. The insurance company is obligated to cover medical expenses as well as compensate the injured individual.',
				},
				{
					'id': 'eu_cargo_mercancias',
					'title': 'Freight/Goods Insurance',
					'desc': 'Goods coverage. The insurance company is obligated to bear the purchased sum in case of an accident or total loss of loaded freight (general goods, perishables, electronics, etc.)',
				},
				{
					'id': 'eu_responsabilidad_general',
					'title': 'General Liability',
					'desc': 'Carrier liability that applies when the driver is not at the wheel.',
				},
				{
					'id': 'eu_poliza_auto',
					'title': 'Auto Policy (Private, Border Plates, Domestic, North American)',
					'desc': 'Contracting a civil liability policy guarantees the coverage and repairs to units in the event of an accident on U.S. highways.',
				},
				{
					'id': 'eu_responsabilidad_general_trailer',
					'title': 'General Liability – Non-Identified Trailer-Haul Insurance',
					'desc': 'Coverage for box or platform: In case the equipment moved is not the property of its owner, and the proper owner is a third party, the insurance company is obligated to cover, in its totality, the loss or partial loss of the unit.',
				},				
				{
					'id': 'eu_poliza_exceso',
					'title': 'Excess Policy',
					'desc': 'An additional individual coverage policy for major medical expenses or other types of risks. It usually operates upon a prior primary policy purchased, with the insured sum that allows addressing expenses not covered in the primary policy.',
				},
				{				
					'id': 'eu_seguro_traslado',
					'title': 'Travel Insurance by Day (1, 3 & 7 days) in the U. S.',
					'desc': 'Civil liability coverage per trip, purchased for trucks departing from one point to its final destination. This applies to units without commercial permits and most of that are without plate registration from the DMV. Units are protected with property documentation and insurance.',
				},
			]
			
		]		
		return data[lang]

	def mx(self, lang=0):
		data = [
			[
				{
					'id': 'mx_default',					
					'desc': '<p><strong>Servicios Garita Otay</strong> le brinda las mejores opciones para protección en la industria. Nuestros clientes encontrarán una amplia gama de productos ante compañías certificadas y confiables del país. </p><p>En Servicios Garita Otay somos agentes directos y autorizados por la Comisión de Seguros y Fianzas de México.</p>',
				},				
				{
					'id': 'mx_responsavilidad_civil',
					'title': 'Responsabilidad Civil en México - Autos y Camiones',
					'desc': 'El contrato de seguro cubre daños a terceros a la propiedad de un bien, así  mismo, cubre los gastos médicos de los ocupantes. Dichos vehículos son de procedencia mexicana y de uso particular o comercial.',
				},
				{
					'id': 'mx_poliza_turisiticas',
					'title': 'Pólizas Turísticas de Auto',
					'desc': 'Cobertura de responsabilidad civil en México con procedencia extranjera. La póliza aplica a vehículos que se internan en el territorio mexicano, los cuales tienen el beneficio de estar protegidos con diversas coberturas.',
				},				
				{
					'id': 'mx_poliza_turisiticas_comerciales',
					'title': 'Pólizas Turísticas Comerciales (Tractores)',
					'desc': 'Cobertura de responsabilidad civil en México con procedencia extranjera o con permiso mexicano Transfer.',
				},				
				{
					'id': 'mx_poliza_20',
					'title': 'Pólizas de Transfer, 20 Km',
					'desc': 'Cobertura de responsabilidad civil en la zona fronteriza. Esta póliza está diseñada para unidades de carga que cruzan a territorio mexicano con un límite de internación.',
				},
				{
					'id': 'mx_cobertura_amplia',
					'title': 'Cobertura Amplia - Auto y Comercial',
					'desc': 'Cobertura total amplia por robo, pérdida parcial o total de la propiedad, responsabilidad civil en bienes y personas, gastos médicos, asesoría legal y jurídica.',
				},
				{				
					'id': 'mx_seguro_carga',
					'title': 'Seguro de Carga - Traslados a México',
					'desc': 'Cobertura contratada por viaje en caso de pérdida de mercancías o robo de la misma. La compañía se obliga a cubrir el monto contratado en los términos del contrato y estatutos de cada caso.',
				},
				{	
					'id': 'mx_gastos_medicos',			
					'title': 'Seguro Gastos Médicos Mayores',
					'desc': 'Para los mexicanos es muy importante contar con una póliza de Gastos Médicos Mayores que permita la atención rápida en centros afiliados y hospitales ante un evento no previsto. Dicha atención también incluye, por ejemplo, consultas familiares, consulta para cirugías y para surtir receta en farmacias afiliadas y el pago de prima por incapacidad.',
				},
				{
					'id': 'mx_casa_habitacion',
					'title': 'Seguro Casa Habitación',
					'desc': 'Es de suma importancia contar con un seguro patrimonial. Dicha póliza  garantiza la cobertura del bien inmueble y bienes materiales y en este contrato especial se especifican detalladamente los artículos o particularidades del bien para asegurarlo en  cualquier eventualidad causada por un terremoto, huracanes o robo en casa habitación, por mencionar algunos desastres o siniestros.',
				},
				{
					'id': 'mx_repatriacion',
					'title': 'Seguros de Repatriación',
					'desc': 'Cobertura en el extranjero por fallecimiento, repatriación de los restos, gestoría de trámites por parte de la compañía de seguros, obtención de  las licencias y permisos para su transportación a México o Centroamérica.',
				},
				{
					'id': 'mx_seguro_vida',
					'title': 'Seguro de Vida',
					'desc': 'El seguro de vida actúa como resguardo frente a una posible dificultad económica donde el beneficiario recibirá una suma de dinero en caso del  fallecimiento del titular. Es una forma de brindar tranquilidad y seguridad tanto al contratante como a sus seres queridos.',
				},
				{
					'id': 'mx_educacion_retiro',
					'title': 'Seguro Educación y Retiro',
					'desc': 'El seguro de educación permite garantizar los estudios profesionales de sus hijos de manera permanente. Por su parte, el seguro de retiro se apoya en sus ahorros y le otorga el beneficio en la vejez y el  bienestar para vivir plenamente.',
				},
			],
			[
				{
					'id': 'mx_default',
					'desc': '<p><strong>Servicios Garita Otay</strong> offers you the best options for insurance protection in the industry. Our clients find a wide range of products from certified and trustworthy companies in the country.</p><p>Personnel at the company are direct insurance agents authorized by the Mexican Insurance and Bond Commission.</p>',
				},				
				{
					'id': 'mx_responsavilidad_civil',
					'title': 'Civil Liability in Mexico - Autos and Trucks',
					'desc': 'The insurance contract covers damage to third party property, as well as medical expenses to the passengers. These vehicles are from Mexican origin and of commercial or private use.',
				},
				{
					'id': 'mx_poliza_turisiticas',
					'title': 'Auto Touristic Policies',
					'desc': 'Auto Touristic Policies are civil liability coverage for foreign vehicles that go into Mexican territory. These units shall have the benefit of being protected by diverse coverage.',
				},				
				{
					'id': 'mx_poliza_turisiticas',
					'title': 'Touristic Commercial Policies (Tractors)',
					'desc': 'Touristic Commercial Policies are civil liability coverage for foreign origin units or with a Mexican Transfer permit.',
				},				
				{
					'id': 'mx_poliza_20',
					'title': 'Transfer Policies, 20 Km (12 miles)',
					'desc': 'Civil liability coverage processed at the border. This policy is designed for freight units that cross onto Mexican territory with an entry limit.',
				},
				{
					'id': 'mx_cobertura_amplia',
					'title': 'Full coverage – Auto and Commercial',
					'desc': 'Full coverage for theft, partial or total loss property, civil liability on goods and people, medical expenses and legal consultation.',
				},
				{				
					'id': 'mx_seguro_carga',
					'title': 'Freight Insurance- Travel to Mexico',
					'desc': 'Coverage purchased per trip in the case of loss or stolen goods. The insurance company is obligated to cover the sum purchased according to the contract in each case.',
				},
				{	
					'id': 'mx_gastos_medicos',			
					'title': 'Major Medical Expenses Insurance',
					'desc': 'It is highly important for Mexican residents to have an adequate Major Medical Expense Insurance policy that enables them to get the proper and timely medical assistance, in the most suitable medical facilities, in case of an unexpected event. This medical assistance shall also cover regular medical visits, consultations for surgery and prescription medicines, as well as payment in case of disability.',
				},
				{
					'id': 'mx_casa_habitacion',
					'title': 'Residential Home Insurance',
					'desc': 'It is highly important to have asset insurance. This policy guarantees coverage on your property and details in a contract the items and particularities of your assets in order to be insured in the case of an unexpected event caused by a natural disaster, or theft amongst other events.',
				},
				{
					'id': 'mx_repatriacion',
					'title': 'Repatriation Insurance',
					'desc': 'Coverage in the case of death in a foreign country, repatriation of remains, processing, paperwork with the insurance company, and license and permit acquirement for transportation to Mexico or Central America.',
				},
				{
					'id': 'mx_seguro_vida',
					'title': 'Life Insurance',
					'desc': 'Life insurance protects you in the event of financial difficulties where the beneficiary may receive a sum of money in case the policy holder encounters death. This is a proper way to provide peace of mind and security to both the policy holder and his/her loved ones.',
				},
				{
					'id': 'mx_educacion_retiro',
					'title': 'Education and Retirement Insurance',
					'desc': 'Education insurance allows the contractor to guarantee permanent academic studies for his/her children. On the other hand, retirement insurance relies on the policy holder’s savings and awards the benefit at an elderly age for a full and comfortable well-being.',
				},
			]
			
		]		
		return data[lang]
