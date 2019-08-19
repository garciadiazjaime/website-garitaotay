var folder = '/';
var server = get_server_path() + folder;

$(window).load(function(){
	var page = get_currentpage();
	var last_item = getLastItem(page)

	
	if(last_item.length && $('#' + last_item).length)
		gotoTop(last_item)				

	$('.submenu_element').hover(function(){
		var id_submenu = $(this).attr('id');
		subMenuSelection(id_submenu)
	});	
	
	

	$('#wrapper').animate({
		'opacity': '1'
		}, 'slow'
	);
	
	$('#header_layer .submenu .tramites_permisos, #header_layer .submenu .permisos').hover(function(){
		
		$('#header_layer .submenu .tramites_permisos, #header_layer .submenu .permisos').removeClass('current');
		$(this).addClass('current');	
	});
	
	
	$('#auxiliar_menu_layer #m_tramites_permisos_layer .submenu li').hover(function(){
		
		$('#auxiliar_menu_layer .submenu li').removeClass('current');
		$(this).addClass('current');	});
	
	$('#menu_group').mouseleave(function() { 
	   showMainSubmenu();
	});

	$('.grid li').click(function(){			
		slider = $(this).parent().attr('class')		
		id = $(this).attr('id')
		if(id.indexOf('empty') === -1)
		{
			$('#'+slider).find('.current').removeClass('current')
			$('#'+id+'_slide').addClass('current')	
		}		
		return false
	})	

	$('.slider_navigation li').click(function(){
		slider = $(this).parent().attr('alt')
		element = $('#'+slider).find('.current')
		if($(this).hasClass('next'))
		{
			if(!$(element).hasClass('last'))
			{
				$(element).removeClass('current')
				if($(element).next().attr('id').indexOf('empty') === -1)
						$(element).next().addClass('current')
				else
				{
					if(!$(element).next().hasClass('last'))
						$(element).next().next().addClass('current')
					else
						$('#'+slider).find('.first').addClass('current')
				}					
			}
			else{
				$(element).removeClass('current')
				$('#'+slider).find('.first').addClass('current')
			}
		}else if($(this).hasClass('prev')){
			if(!$(element).hasClass('first'))
			{
				$(element).removeClass('current')
				if($(element).prev().attr('id').indexOf('empty') === -1)
					$(element).prev().addClass('current')
				else
				{
					if(!$(element).prev().hasClass('first'))
						$(element).prev().prev().addClass('current')
					else
						$('#'+slider).find('.last').addClass('current')
				}
			}
			else{
				$(element).removeClass('current')
				if($('#'+slider).find('.last').attr('id').indexOf('empty') === -1)
					$('#'+slider).find('.last').addClass('current')
				else
					$('#'+slider).find('.last').prev().addClass('current')
			}
		}
		return false	
	})

	if($('.slideshow').length)
		$('.slideshow').cycle({
			fx: 'scrollLeft',
			timeout:  8000,
		});

	if($('#map_area').length)
		$('#map_area').html('<iframe width="450" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps/ms?msid=212370376734302597466.0004de86925946a7d7271&amp;msa=0&amp;ie=UTF8&amp;t=m&amp;ll=32.542888,-116.943115&amp;spn=0.040445,0.091925&amp;output=embed"></iframe><br /><small><a href="https://maps.google.com/maps/ms?msid=212370376734302597466.0004de86925946a7d7271&amp;msa=0&amp;ie=UTF8&amp;t=m&amp;ll=32.542888,-116.943115&amp;spn=0.040445,0.091925&amp;source=embed" style="color:#0000FF;text-align:left" target="_blank">View  in a larger map</a></small>')

	if($('#contact_form').length)
	{		
		$("#contact_form").submit(function() {
			console.log('here')
			flag = true
			if($('#name').val() == '')
			{
				$('#name').prev().addClass('required')
				flag = false
			}
			else
				$('#name').prev().removeClass('required')

			if($('#email').val() == '')
			{
				$('#email').prev().addClass('required')
				flag = false
			}
			else
				$('#email').prev().removeClass('required')

			if($('#message').val() == '')
			{
				$('#message').prev().addClass('required')
				flag = false
			}
			else
				$('#message').prev().removeClass('required')			

			if(!flag)
				$('#msg').html('Favor de llenar los campos marcados')
			else
			{
				if(isValidEmailAddress($('#email').val()))
				{					
					$('#msg').html('Enviando datos, por favor espera...')
					$.post("send_mail", $(this).serialize(), function(data) {
						if(data == 'success')
						{
							$('#msg').html('Gracias tu mensaje ha sido enviado.')
							clearForm()
						}						
						else if(data == 'empty_data')
							$('#msg').html('Favor de intenarlo de nuevo')
						else
							$('#msg').html('Lo sentimos, tu mensaje no fue enviado, por favor intenta m\xE1s tarde.')
					});
				}
				else
				{
					$('#msg').html('Favor captura run email v\xE1lido')
				}
			}
			return false;
		});		
	}
});

function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
}

function get_currentpage(){
	var loc = window.location;
	p = loc.href.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length );
	if(p == '') p = 'inicio';
	return p;
}

function gotoTop(id, speed , more){
	if(isNaN(speed))
		speed = 1250
	if(isNaN(more))
		more = 0

	if(id.length)
		$('html, body').animate({
			scrollTop: $('#'+id).offset().top + more
		}, speed);
}

function isFormReady() {
	var formChildren = $("form :input[type=text]"); // verificar inputs
	var flag = true;
	for (i = 0; i < (formChildren.length); i++) {
		if (formChildren[i].lang == 'es' && formChildren[i].value == '') {
				flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}

	var formChildren = $('select'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		if ($(formChildren[i]).attr('lang') == 'es' && $(formChildren[i]).val() == 0) {
			if (flag) flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}

	var formChildren = $('textarea'); // textarea
	for (i = 0; i < (formChildren.length); i++) {
		if (formChildren[i].lang == 'es' && formChildren[i].value == '') {
			if (flag)
				flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}
	return flag;
}

function clearForm(){
	var formChildren = $("form :input[type=text]");
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val('');
	}

	var formChildren = $("form :input[type=checkbox]");
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).attr('checked', false);
	}

	var formChildren = $("form :input[type=email]");
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val('');
	}

	var formChildren = $('select'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val(0);
	}

	var formChildren = $('textarea'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val('');
	}
}

function getLastItem(cadena){
       var params = cadena.split('/');
       return params.pop();
}


function get_server_path(){
	var loc = window.location;
	return "http://" + loc.hostname;
}

function subMenuSelection(id){	
	if(id){	
		$('.submenu_element').removeClass('current');
		$('.submenu_element ul').removeClass('active');
		$('#'+id).addClass('current');
		if('#'+id+'_list'){
			$('#'+id+'_list').addClass('active');
		}
	}
}

function hideMainSubmenu(){
	var currentClass = $('#header_layer').attr('class');
	if(currentClass=='visible'){
		$('#header_layer').removeClass('visible');
		$('#header_layer').addClass('invisible');
		$('#auxiliar_menu_layer').removeClass('invisible');
		$('#auxiliar_menu_layer').addClass('visible');
	}
}

function showMainSubmenu(){
	var currentClass = $('#header_layer').attr('class');
	if(currentClass=='invisible'){
		$('#header_layer').removeClass('invisible');
		$('#header_layer').addClass('visible');
		$('#auxiliar_menu_layer').removeClass('visible');
		$('#auxiliar_menu_layer').addClass('invisible');
	}
}

function showCorrectSubmenu(id){
	$('#auxiliar_menu_layer div').removeClass('current');
	$('#'+id+'_layer').addClass('current');
}