from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # nombre de la vista principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CrearUsuarioForm, CrearAdminForm

def crear_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('crear_usuario')
    else:
        form = CrearUsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def crear_admin(request):
    if request.method == 'POST':
        form = CrearAdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True      # puede entrar al admin
            user.is_superuser = True  # tiene permisos de todo
            user.save()
            return redirect('crear_admin')
    else:
        form = CrearAdminForm()
    return render(request, 'usuarios/crear_admin.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registrar_usuario')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return redirect('registrar_usuario')

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Usuario creado exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'usuarios/registrar.html')
