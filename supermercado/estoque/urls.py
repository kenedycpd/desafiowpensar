from django.urls import include, path
from . import views
urlpatterns = [
     path('cadastro/', views.cadastro, name='cadastro'),
     path('compra/', views.compra, name='compra'),
     path('lista/', views.lista, name='lista'),
]