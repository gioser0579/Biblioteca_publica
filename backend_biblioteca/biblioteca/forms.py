from django import forms
from .models import Socio, Bibliotecario, Prestamo, Libro, Autor, Editorial, Multa

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'

class BibliotecarioForm(forms.ModelForm):
    class Meta:
        model = Bibliotecario
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = '__all__'
