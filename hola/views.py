from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hola, este es la base de la Aplicacion llamada <hola>")

def lahora(request):

    dt = datetime.datetime.now()
    context = {"dt": dt}

    return render(request, 'vhora.html', context)
