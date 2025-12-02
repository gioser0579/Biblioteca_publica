from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AutorViewSet, EditorialViewSet, LibroViewSet, SocioViewSet, BibliotecarioViewSet, PrestamoViewSet, MultaViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'bibliotecarios', BibliotecarioViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'multas', MultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
