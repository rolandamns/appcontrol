from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import persona, actividad
from allauth.account.decorators import verified_email_required



# @verified_email_required
def principal(request):
    return render(request,'appcontrol/principal.html')

# @verified_email_required

def home(request):

    try:
        # entry = persona.objects.get(telefono='mrolando.antonio@unsch.edu.pe')
        entry = persona.objects.get(telefono=request.POST["correo"])
        
        print(entry.dni)

        # actividades = actividad.objects.filter(dni=dni_empleado)
        actividades = actividad.objects.filter(dni=entry.dni)
        data = {
            'actividades': actividades
        }
        return render(request,'appcontrol/informes.html',data)

    except persona.DoesNotExist:
        # raise Http404("No MyModel matches the given query.")
        return render(request,'appcontrol/correo_no_registrado.html')
    
  