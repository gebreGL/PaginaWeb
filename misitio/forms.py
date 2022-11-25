from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [ 'dni', 'nombre', 'fechaAlta', 'correo', 'movil']

        # también se podría hacer  --> ya que queremos todos los campos
        # class Meta:
        #   model = Canciones
        #   fields = '__all__'