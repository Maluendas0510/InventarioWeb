from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Producto
from .forms import ProductoForm

def es_admin(user):
    return user.is_staff or user.is_superuser


# Create your views here.
def index(request):
    return render(request, 'post/index.html')

@login_required
def inicio(request):
    return render(request, 'post/inicio.html')

@login_required
@user_passes_test(es_admin)
def categorias(request):
    return render(request, 'post/categorias.html')

@login_required
@user_passes_test(es_admin)
def proveedores(request):
    return render(request, 'post/proveedores.html') 

@login_required
@user_passes_test(es_admin)
def productos(request):
    # Obtener todos los productos de la base de datos
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Redirige después de guardar
    else:
        form = ProductoForm()

    return render(request, 'post/productos.html', {
        'productos': productos,
        'form': form
    })
