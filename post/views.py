from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Producto
from .forms import ProductoForm



# Create your views here.
def index(request):
    return render(request, 'post/index.html')

@login_required
def categorias(request):
    return render(request, 'post/categorias.html')

@login_required
def proveedores(request):
    return render(request, 'post/proveedores.html') 

@login_required
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
