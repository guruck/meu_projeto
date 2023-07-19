"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from meu_app import views


urlpatterns = [
    path('', RedirectView.as_view(url='/agenda')),
    path('agenda/', views.lista_eventos),
    path('agenda/evento', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('login/submit', views.submit_login),
    path('soma/<int:numeroa>/<int:numerob>', views.soma),
    # path('', views.index)
]
