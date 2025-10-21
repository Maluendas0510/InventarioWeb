from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categoria, Proveedor, Producto
from .forms import ProductoForm, CategoriaForm, ProveedorForm
from django.shortcuts import render, redirect, get_object_or_404


def es_admin(user):
    return user.is_superuser

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

def es_admin(user):
    return user.is_superuser

@login_required
def categorias(request):
    categorias = Categoria.objects.all()

   
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('categorias')
        else:
            form = CategoriaForm()
    else:
        form = None

    return render(request, 'post/categorias.html', {
        'categorias': categorias,
        'form': form,
    })

@user_passes_test(es_admin)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'post/editar_categoria.html', {'form': form, 'categoria': categoria})

@user_passes_test(es_admin)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('categorias')


@login_required
def proveedores(request):
    proveedores = Proveedor.objects.all()

    # Solo los administradores pueden agregar proveedores
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProveedorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('proveedores')
        else:
            form = ProveedorForm()
    else:
        form = None  # Los usuarios normales solo pueden ver

    return render(request, 'post/proveedores.html', {
        'proveedores': proveedores,
        'form': form
    })


@login_required
def productos(request):
    productos = Producto.objects.all()

    # Solo los administradores pueden agregar productos
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('productos')
        else:
            form = ProductoForm()
    else:
        form = None  # Los usuarios normales solo pueden ver

    return render(request, 'post/productos.html', {
        'form': form,
        'productos': productos
    })



@login_required
def informacion(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    # Si el usuario no es admin, puede modificar stock
    if request.method == 'POST' and not (hasattr(request.user, 'usuario') and request.user.usuario.rol.lower() == 'admin'):
        producto_id = request.POST.get('producto_id')
        stock_actual = request.POST.get('stock_actual')
        stock_minimo = request.POST.get('stock_minimo')

        producto = get_object_or_404(Producto, id=producto_id)
        producto.stock_actual = stock_actual
        producto.stock_minimo = stock_minimo
        producto.save()

        return redirect('informacion')

    return render(request, 'post/informacion.html', {
        'categorias': categorias,
        'productos': productos,
        'proveedores': proveedores
    })
