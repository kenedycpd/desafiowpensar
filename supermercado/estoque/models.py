from django.db import models

# Create your models here.
class Cadastro_Prod(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=200, verbose_name='Descricao do Produto')
	def __str__(self):
		return self.nome


class Compra(models.Model):
	id = models.AutoField(primary_key=True)
	produto = models.CharField(max_length=200,verbose_name='Descricao do Produto')
	quantidade = models.IntegerField(verbose_name='Qunatidade do Produto')
	preco_compra = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Preço do Produto')

	def calculo(self):
		return self.preco_compra / self.quantidade
	media = property(calculo)
	
	def __str__(self):
		return self.produto

