from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from .forms import ProductoForm

def es_admin(user):
    return user.is_staff or user.is_superuser

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
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')  
    else:
        form = ProductoForm()

    return render(request, 'post/productos.html', {
        'productos': productos,
        'form': form
    })

from .models import Categoria, Producto, Proveedor

@login_required
@user_passes_test(es_admin)
def informacion(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'post/informacion.html', {
        'categorias': categorias,
        'productos': productos,
        'proveedores': proveedores
    })

@login_required
def inicio(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'post/inicio.html', {
        'categorias': categorias,
        'productos': productos,
        'proveedores': proveedores
    })
