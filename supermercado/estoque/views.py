from django.shortcuts import render, redirect
from .models import Cadastro_Prod, Compra
from .forms import CadastroForm, CompraForm
# Create your views here.
def home(request):
	return render(request, 'index.html')


def cadastro(request):
	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CadastroForm()
	return render(request, 'estoque/cadastro.html',{'form':form})


def compra(request):
	if request.method == 'POST':
		form = CompraForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CompraForm()
	return render(request, 'estoque/compra.html',{'form':form})



def lista(request):
	compras = Compra.objects.all()
	return render(request, 'estoque/lista.html',{'compras':compras})