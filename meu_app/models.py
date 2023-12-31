from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone


# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True,
                                        verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        # .replace(tzinfo=timezone(offset=timedelta()))
        return self.data_evento < datetime.now()

    def get_data_criacao_input(self):
        return self.data_criacao.strftime('%Y-%m-%dT%H:%M')


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50, null=False)
    ico = models.CharField(max_length=50, null=True)
    elevate = models.BooleanField(null=False, default=False)
    page = models.CharField(max_length=50, null=False)
    ativo = models.BooleanField(null=False, default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'menus'

    def __str__(self):
        return self.name

    def get_data_evento(self):
        return self.updated.strftime('%d/%m/%Y %H:%M')
