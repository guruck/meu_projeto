"""modulo responsavel pela interpretacao e devolucao das paginas
"""
from django.shortcuts import HttpResponse, render, redirect
from meu_app.models import Evento, Menu
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def get_base(**kwargs):
    menus = Menu.objects.all()
    dados = {'menus': menus}
    dados.update(kwargs)
    return dados


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
def lista_eventos(request, **kargs):
    """funcao que lista os eventos agendados
    """
    # evento = Evento.objects.all()  # get(id=1)
    evento = Evento.objects.filter(usuario=request.user)
    dados = {'eventos': evento}
    args = {"icon": "icofont-navigation-menu",
            "titulo": "Cadastro de Eventos",
            "subtitulo": "Mantenha os dados dos eventos atualizados"}
    dados.update(get_base(**args))
    if kargs.get('message'):
        dados['message'] = kargs.get('message')

    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    """funcao que lista os eventos agendados
    """
    if request.POST:
        auxid = request.POST.get('id')
        titulo = request.POST.get('evtitulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        usuario = request.user

        if auxid:
            Evento.objects.filter(id=auxid, usuario=usuario).update(
                titulo=titulo, descricao=descricao, data_evento=data_evento,
            )
        else:
            Evento.objects.create(titulo=titulo,
                                  descricao=descricao,
                                  data_evento=data_evento,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    """funcao que lista os eventos agendados
    """
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
        if usuario == evento.usuario:
            evento.delete()
    except Exception as e:
        return lista_eventos(request, **{'message': e})

    return redirect('/')

def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request, id_evento: int = None):
    args = {"icon": "icofont-navigation-menu",
            "titulo": "Cadastro de Eventos",
            "subtitulo": "Crie e atualize o evento"}
    if id_evento is not None:
        args["evento"] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', args)


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
