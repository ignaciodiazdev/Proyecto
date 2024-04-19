from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola Django!")


def saludo_vista(request):
    return HttpResponse("<h1>Segunda Vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f'<h1>{apellido}, {nombre}</h1>')


def probando_template(request):
    mi_html = open('./templates/template1.html', encoding="UTF-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({'saludo': '¡Bienvenido!'})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

# def nombre(request, nombre: str, apellido: str):

#     context = {
#         'persona': [
#             {
#                 'nombre': nombre.capitalize(),
#                 'apellido': apellido.capitalize()
#             }
#         ]
#     }
