from django.http import HttpResponse
from django.views.generic import ListView
from .models import Usuario, Membresia, Acceso, RegistroBiometrico, Empleado


class HomePageView(ListView):
    model = Usuario
    template_name = "home.html"
