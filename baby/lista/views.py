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
		return HttpResponseRedirect('/mensajerecibido')

    return render_to_response('regalo.html', {'regalo':regalo,},context_instance=RequestContext(request))


def home(request):
    regalos = Regalo.objects.all()
    
    return render_to_response(
        "home.html", {'regalos':regalos,},context_instance=RequestContext(request))

def estudiantes(request):
	return render_to_response('estudiantes.html',context_instance=RequestContext(request))

