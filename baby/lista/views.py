# Create your views here
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import EmailMessage
from lista.models import Categoria, Regalo

def one_regalo(request, idregalo):
    regalo = Regalo.objects.get(id=idregalo)

    if request.method=='POST':
		nombre=request.POST['nombre']
		email=request.POST['email']
		mensaje=request.POST['mensaje']
		regalo=request.POST['regalo']

		titulo = 'Nuevo regalo shower'
		contenido = 'Nombre: ' + nombre + "\n"
		contenido += 'Email: ' + email + "\n"	
		contenido += 'Mensaje: ' + mensaje + "\n"
		contenido += 'Regalo: ' + regalo
		correo = EmailMessage(titulo, contenido, to=['jdaarevalo@gmail.com'])
		correo.send()

		from django.core.mail import EmailMultiAlternatives
		from django.template.loader import get_template
		from django.template import Context
			
		plaintext = get_template('regalo_seleccionado.txt')
		htmly     = get_template('regalo_seleccionado.html')
		regalo_s = Regalo.objects.get(id=idregalo)
		d = Context({ 'regalo':regalo_s})

		subject, from_email, to = 'Regalo para Juan David', 'info@ukanbook.com', email
		text_content = plaintext.render(d)
		html_content = htmly.render(d)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		return HttpResponseRedirect('/mensajerecibido/%s' % (idregalo))

    return render_to_response('regalo.html', {'regalo':regalo,},context_instance=RequestContext(request))


def home(request):
    regalos = Regalo.objects.all()
    
    return render_to_response(
        "home.html", {'regalos':regalos,},context_instance=RequestContext(request))

def mensajerecibido(request, idregalo):
	regalo = Regalo.objects.get(id=idregalo)

	return render_to_response('mensajerecibido.html', {'regalo':regalo,}, context_instance=RequestContext(request))

