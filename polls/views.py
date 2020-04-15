from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Indice de APP de encuestas (Polls).")

def detail(request, question_id):
    return HttpResponse("Consultando la Pregunta: %s" % question_id)

def results(request, question_id):
    response = "Resultados a la Pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Has Votado para la Pregunta %s." % question_id)
