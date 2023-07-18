from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def index(request):

    doc_externo = get_template('index.html')

    documento = doc_externo.render()

    return HttpResponse(documento)

def login(request):

    doc_externo = get_template('login.html')

    documento = doc_externo.render()

    return HttpResponse(documento)

def contactenos(request):

    doc_externo = get_template('contactenos.html')

    documento = doc_externo.render()

    return HttpResponse(documento)

def nosotros(request):

    doc_externo = get_template('nosotros.html')

    documento = doc_externo.render()

    return HttpResponse(documento)

def tienda(request):

    doc_externo = get_template('tienda.html')

    documento = doc_externo.render()

    return HttpResponse(documento)

def compras(request):

    doc_externo = get_template('compras.html')

    documento = doc_externo.render()

    return HttpResponse(documento)