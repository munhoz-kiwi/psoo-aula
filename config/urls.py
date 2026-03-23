from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # Listagens
    path('livros/', LivrosView.as_view(), name='livros'),
    #path('reserva/', EmprestimoView.as_view(), name='reserva'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('autor/', AutoresView.as_view(), name='autor'),
    path('editor/', EditorasView.as_view(), name='editora'),
    path('leitor/', LeitoresView.as_view(), name='leitor'),
    path('genero/', GenerosView.as_view(), name='genero'),]
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', ConsultaView.as_view(), name='livros'),
    #path('reserva/', ReservaView.as_view(),
#name='reserva'),
    path('delete/<int:id>/', DeleteLivroView.as_view(),
name='delete'),
]