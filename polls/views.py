from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question

def index(request):
    # return HttpResponse("Indice de APP de encuestas (Polls).")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Consultando la Pregunta: %s" % question_id)

def results(request, question_id):
    response = "Resultados a la Pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Has Votado para la Pregunta %s." % question_id)
