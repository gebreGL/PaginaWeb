from . import views
from django.urls import path

urlpatterns = [
    path('', views.cliente_list, name="clientes_list"),
    path('cliente/new', views.clientes_new, name='cliente_new'),
]