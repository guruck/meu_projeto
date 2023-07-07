"""modulo responsavel pela interpretacao e devolucao das paginas
"""
from django.shortcuts import HttpResponse, render  # , redirect
from meu_app.models import Evento

# Create your views here.
def hello(_):
    """funcao inicial

    Returns:
        retorna um ola mundo para saber que a aplicacao funciona
    """
    return HttpResponse('Hello-World')


def soma(_, numeroa: int, numerob: int):
    """funcao para somar dois valores por parametro na url

    Arguments:
        numeroa -- inteiro numerico
        numerob -- inteiro numerico

    Returns:
        a soma dos argumentos informados
    """
    total = numeroa + numerob
    return HttpResponse(f'A soma dos parametros é {total}')


def lista_eventos(request):
    """funcao que lista os eventos agendados
    """
    evento = Evento.objects.all()  # get(id=1)
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


# def index(_):
#     return redirect('/agenda/')
