from django.contrib import admin
from .models import Autor, Editorial, Socio, Bibliotecario, Libro, Prestamo, Multa

# Register your models here.
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Socio)
admin.site.register(Bibliotecario)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Multa)
