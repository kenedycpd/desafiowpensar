from django.forms import ModelForm
from .models import *

class CadastroForm(ModelForm):
	class Meta:
		model = Cadastro_Prod
		fields = '__all__'


class CompraForm(ModelForm):
	class Meta:
		model = Compra
		fields = '__all__'