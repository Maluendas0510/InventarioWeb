from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
   
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('productos/', views.productos, name='productos'),
    path('informacion/', views.informacion, name='informacion'),      
]