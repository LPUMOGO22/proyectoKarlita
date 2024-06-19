from django.contrib import admin
from .models import Usuario, Membresia, Acceso, RegistroBiometrico, Empleado

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Membresia)
admin.site.register(Acceso)
admin.site.register(RegistroBiometrico)
admin.site.register(Empleado)
