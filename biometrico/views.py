from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Usuario, Membresia, Acceso, RegistroBiometrico, Empleado


class HomePageView(ListView):
    model = Usuario
    template_name = "home.html"


# | ---------------------------------------------------- |
# | ---------------------------------------------------- |
# |      Vistas Relacionadas al modelo "Usuario"         |
# | ---------------------------------------------------- |
# | ---------------------------------------------------- |


class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuario/usuariosList.html"


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuario/usuarioDetail.html"


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = "usuario/usuarioCreate.html"
    fields = [
        "nombre",
        "apellido",
        "email",
        "telefono",
        "direccion",
        "fecha_nacimiento",
        "genero",
        "estado_civil",
        "profesion",
        "fecha_ingreso",
        "fecha_egreso",
        "estado",
        "membresia",
        "empleado",
    ]
    success_url = "/usuarios"


class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = "usuario/usuarioUpdate.html"
    fields = [
        "nombre",
        "apellido",
        "email",
        "telefono",
        "direccion",
        "fecha_nacimiento",
        "genero",
        "estado_civil",
        "profesion",
        "fecha_ingreso",
        "fecha_egreso",
        "estado",
        "membresia",
        "empleado",
    ]
    success_url = "/usuarios"


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/usuarioDelete.html"
    success_url = "/usuarios"


# | ---------------------------------------------------- |
# | ---------------------------------------------------- |
# |      Vistas Relacionadas al modelo "Membresia"       |
# | ---------------------------------------------------- |
# | ---------------------------------------------------- |


class MembresiaListView(ListView):
    model = Membresia
    template_name = "membresia/membresiasList.html"


class MembresiaDetailView(DetailView):
    model = Membresia
    template_name = "membresia/membresiaDetail.html"


class MembresiaCreateView(CreateView):
    model = Membresia
    template_name = "membresia/membresiaCreate.html"
    fields = [
        "nombre",
        "descripcion",
        "precio",
        "duracion",
        "estado",
    ]
    success_url = "/membresias"


class MembresiaUpdateView(UpdateView):
    model = Membresia
    template_name = "membresia/membresiaUpdate.html"
    fields = [
        "nombre",
        "descripcion",
        "precio",
        "duracion",
        "estado",
    ]
    success_url = "/membresias"


class MembresiaDeleteView(DeleteView):
    model = Membresia
    template_name = "membresia/membresiaDelete.html"
    success_url = "/membresias"


# | ---------------------------------------------------- |
# | ---------------------------------------------------- |
# |      Vistas Relacionadas al modelo "Acceso"          |
# | ---------------------------------------------------- |
# | ---------------------------------------------------- |


class AccesoListView(ListView):
    model = Acceso
    template_name = "acceso/accesosList.html"


class AccesoDetailView(DetailView):
    model = Acceso
    template_name = "acceso/accesoDetail.html"


class AccesoCreateView(CreateView):
    model = Acceso
    template_name = "acceso/accesoCreate.html"
    fields = [
        "fecha",
        "hora_entrada",
        "hora_salida",
        "estado",
        "usuario",
    ]
    success_url = "/accesos"


class AccesoUpdateView(UpdateView):
    model = Acceso
    template_name = "acceso/accesoUpdate.html"
    fields = [
        "fecha",
        "hora_entrada",
        "hora_salida",
        "estado",
        "usuario",
    ]
    success_url = "/accesos"


class AccesoDeleteView(DeleteView):
    model = Acceso
    template_name = "acceso/accesoDelete.html"
    success_url = "/accesos"


# | ------------------------------------------------------- |
# | ------------------------------------------------------- |
# |   Vistas Relacionadas al modelo "RegistroBiometrico"    |
# | ------------------------------------------------------- |
# | ------------------------------------------------------- |


class RegistroBiometricoListView(ListView):
    model = RegistroBiometrico
    template_name = "registro_biometrico/registrosBiometricosList.html"


class RegistroBiometricoDetailView(DetailView):
    model = RegistroBiometrico
    template_name = "registro_biometrico/registroBiometricoDetail.html"


class RegistroBiometricoCreateView(CreateView):
    model = RegistroBiometrico
    template_name = "registro_biometrico/registroBiometricoCreate.html"
    fields = [
        "fecha",
        "hora",
        "estado",
        "usuario",
    ]
    success_url = "/registros-biometricos"


class RegistroBiometricoUpdateView(UpdateView):
    model = RegistroBiometrico
    template_name = "registro_biometrico/registroBiometricoUpdate.html"
    fields = [
        "fecha",
        "hora",
        "estado",
        "usuario",
    ]
    success_url = "/registros-biometricos"


class RegistroBiometricoDeleteView(DeleteView):
    model = RegistroBiometrico
    template_name = "registro_biometrico/registroBiometricoDelete.html"
    success_url = "/registros-biometricos"


# | ---------------------------------------------------- |
# | ---------------------------------------------------- |
# |      Vistas Relacionadas al modelo "Empleado"        |
# | ---------------------------------------------------- |
# | ---------------------------------------------------- |


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/empleadosList.html"


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/empleadoDetail.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/empleadoCreate.html"
    fields = [
        "nombre",
        "apellido",
        "email",
        "telefono",
        "direccion",
        "fecha_nacimiento",
        "genero",
        "estado_civil",
        "profesion",
        "fecha_ingreso",
        "fecha_egreso",
        "estado",
        "usuario",
    ]
    success_url = "/empleados"


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/empleadoUpdate.html"
    fields = [
        "nombre",
        "apellido",
        "email",
        "telefono",
        "direccion",
        "fecha_nacimiento",
        "genero",
        "estado_civil",
        "profesion",
        "fecha_ingreso",
        "fecha_egreso",
        "estado",
        "usuario",
    ]
    success_url = "/empleados"


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/empleadoDelete.html"
    success_url = "/empleados"
