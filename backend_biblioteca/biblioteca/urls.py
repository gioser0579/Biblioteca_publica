from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # URLs para Socios
    path('socios/', views.listar_socios, name='listar_socios'),
    path('socio/agregar/', views.agregar_socio, name='agregar_socio'),
    path('socio/<int:pk>/', views.ver_socio, name='ver_socio'),
    path('socio/<int:pk>/actualizar/', views.actualizar_socio, name='actualizar_socio'),
    path('socio/<int:pk>/borrar/', views.borrar_socio, name='borrar_socio'),

    # URLs para Bibliotecarios
    path('bibliotecarios/', views.listar_bibliotecarios, name='listar_bibliotecarios'),
    path('bibliotecario/agregar/', views.agregar_bibliotecario, name='agregar_bibliotecario'),
    path('bibliotecario/<int:pk>/', views.ver_bibliotecario, name='ver_bibliotecario'),
    path('bibliotecario/<int:pk>/actualizar/', views.actualizar_bibliotecario, name='actualizar_bibliotecario'),
    path('bibliotecario/<int:pk>/borrar/', views.borrar_bibliotecario, name='borrar_bibliotecario'),

    # URLs para Préstamos
    path('prestamos/', views.listar_prestamos, name='listar_prestamos'),
    path('prestamo/agregar/', views.agregar_prestamo, name='agregar_prestamo'),
    path('prestamo/<int:pk>/', views.ver_prestamo, name='ver_prestamo'),
    path('prestamo/<int:pk>/actualizar/', views.actualizar_prestamo, name='actualizar_prestamo'),
    path('prestamo/<int:pk>/borrar/', views.borrar_prestamo, name='borrar_prestamo'),

    # URLs para Libros
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libro/agregar/', views.agregar_libro, name='agregar_libro'),
    path('libro/<int:pk>/', views.ver_libro, name='ver_libro'),
    path('libro/<int:pk>/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('libro/<int:pk>/borrar/', views.borrar_libro, name='borrar_libro'),

    # URLs para Autores
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autor/agregar/', views.agregar_autor, name='agregar_autor'),
    path('autor/<int:pk>/', views.ver_autor, name='ver_autor'),
    path('autor/<int:pk>/actualizar/', views.actualizar_autor, name='actualizar_autor'),
    path('autor/<int:pk>/borrar/', views.borrar_autor, name='borrar_autor'),

    # URLs para Editoriales
    path('editoriales/', views.listar_editoriales, name='listar_editoriales'),
    path('editorial/agregar/', views.agregar_editorial, name='agregar_editorial'),
    path('editorial/<int:pk>/', views.ver_editorial, name='ver_editorial'),
    path('editorial/<int:pk>/actualizar/', views.actualizar_editorial, name='actualizar_editorial'),
    path('editorial/<int:pk>/borrar/', views.borrar_editorial, name='borrar_editorial'),

    # URLs para Multas
    path('multas/', views.listar_multas, name='listar_multas'),
    path('multa/agregar/', views.agregar_multa, name='agregar_multa'),
    path('multa/<int:pk>/', views.ver_multa, name='ver_multa'),
    path('multa/<int:pk>/actualizar/', views.actualizar_multa, name='actualizar_multa'),
    path('multa/<int:pk>/borrar/', views.borrar_multa, name='borrar_multa'),
]
