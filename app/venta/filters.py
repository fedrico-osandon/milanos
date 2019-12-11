
from .models import Cliente, Empleado,Persona
import django_filters


class EmpleadoFilter(django_filters.FilterSet):
    nombres = django_filters.CharFilter(label=False,)
    apellidos = django_filters.CharFilter(label=False,)
    dni = django_filters.CharFilter(label=False,)

    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos', 'dni']


class ClienteFilter(django_filters.FilterSet):
    

    class Meta:
        model = Cliente
        fields = ['persona__nombres', 'persona__apellidos']
