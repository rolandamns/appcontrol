from django.shortcuts import render
from .models import *
from allauth.account.decorators import verified_email_required

from allauth.account.views import SignupView





# @verified_email_required
def home(request):
    actividades = actividad.objects.all()
    data = {
        'actividades': actividades
    }
    return render(request,'appcontrol/index.html',data)


# Create your views here.
