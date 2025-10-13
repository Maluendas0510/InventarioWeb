from django.db import models

# Create your models here.
# es un sistema de inventario basico

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_actual = models.IntegerField(null=True, blank=True)   
    stock_minimo = models.IntegerField(null=True, blank=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre}"

class Detalle_venta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Venta {self.id} - {self.producto.nombre}"
    
class Mov_inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=50)  # Entrada o Salida
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Movimiento {self.id} - {self.producto.nombre}"