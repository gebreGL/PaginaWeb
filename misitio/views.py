
from django.shortcuts import render
from django.utils import timezone

from misitio.forms import ClienteForm
from misitio.models import Cliente


# Create your views here.

def cliente_list(request):
    clientes = Cliente.objects.filter(fechaAlta__lte=timezone.now()).order_by('fechaAlta')
    return render(request, 'misitio/clientes_list.html', {'clientes': clientes})
def clientes_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'misitio/cliente_new.html', {'form': form})