"""modulo responsavel pela interpretacao e devolucao das paginas
"""
from django.shortcuts import HttpResponse, render, redirect
from meu_app.models import Evento
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='/login/')
def lista_eventos(request):
    """funcao que lista os eventos agendados
    """
    # evento = Evento.objects.all()  # get(id=1)
    evento = Evento.objects.filter(usuario=request.user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Usuario ou senha invalido")
    return redirect('/')


# def index(_):
#     return redirect('/agenda/')
