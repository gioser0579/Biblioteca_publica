from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio, Bibliotecario, Prestamo, Libro, Autor, Editorial, Multa
from .forms import SocioForm, BibliotecarioForm, PrestamoForm, LibroForm, AutorForm, EditorialForm, MultaForm

def home(request):
    return render(request, 'home.html')

# Vistas para Socios
def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socio/listar_socios.html', {'socios': socios})

def agregar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm()
    return render(request, 'socio/agregar_socio.html', {'form': form})

def ver_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    return render(request, 'socio/ver_socio.html', {'socio': socio})

def actualizar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socio/actualizar_socio.html', {'form': form})

def borrar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        socio.delete()
        return redirect('listar_socios')
    return render(request, 'socio/borrar_socio.html', {'socio': socio})

# Vistas para Bibliotecarios
def listar_bibliotecarios(request):
    bibliotecarios = Bibliotecario.objects.all()
    return render(request, 'bibliotecario/listar_bibliotecarios.html', {'bibliotecarios': bibliotecarios})

def agregar_bibliotecario(request):
    if request.method == 'POST':
        form = BibliotecarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecarios')
    else:
        form = BibliotecarioForm()
    return render(request, 'bibliotecario/agregar_bibliotecario.html', {'form': form})

def ver_bibliotecario(request, pk):
    bibliotecario = get_object_or_404(Bibliotecario, pk=pk)
    return render(request, 'bibliotecario/ver_bibliotecario.html', {'bibliotecario': bibliotecario})

def actualizar_bibliotecario(request, pk):
    bibliotecario = get_object_or_404(Bibliotecario, pk=pk)
    if request.method == 'POST':
        form = BibliotecarioForm(request.POST, instance=bibliotecario)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecarios')
    else:
        form = BibliotecarioForm(instance=bibliotecario)
    return render(request, 'bibliotecario/actualizar_bibliotecario.html', {'form': form})

def borrar_bibliotecario(request, pk):
    bibliotecario = get_object_or_404(Bibliotecario, pk=pk)
    if request.method == 'POST':
        bibliotecario.delete()
        return redirect('listar_bibliotecarios')
    return render(request, 'bibliotecario/borrar_bibliotecario.html', {'bibliotecario': bibliotecario})

# Vistas para Préstamos
def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo/listar_prestamos.html', {'prestamos': prestamos})

def agregar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamo/agregar_prestamo.html', {'form': form})

def ver_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, 'prestamo/ver_prestamo.html', {'prestamo': prestamo})

def actualizar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamo/actualizar_prestamo.html', {'form': form})

def borrar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('listar_prestamos')
    return render(request, 'prestamo/borrar_prestamo.html', {'prestamo': prestamo})

# Vistas para Libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libro/listar_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libro/agregar_libro.html', {'form': form})

def ver_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libro/ver_libro.html', {'libro': libro})

def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro/actualizar_libro.html', {'form': form})

def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libro/borrar_libro.html', {'libro': libro})

# Vistas para Autores
def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor/listar_autores.html', {'autores': autores})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'autor/agregar_autor.html', {'form': form})

def ver_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'autor/ver_autor.html', {'autor': autor})

def actualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/actualizar_autor.html', {'form': form})

def borrar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'autor/borrar_autor.html', {'autor': autor})

# Vistas para Editoriales
def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editorial/listar_editoriales.html', {'editoriales': editoriales})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm()
    return render(request, 'editorial/agregar_editorial.html', {'form': form})

def ver_editorial(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    return render(request, 'editorial/ver_editorial.html', {'editorial': editorial})

def actualizar_editorial(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm(instance=editorial)
    return render(request, 'editorial/actualizar_editorial.html', {'form': form})

def borrar_editorial(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == 'POST':
        editorial.delete()
        return redirect('listar_editoriales')
    return render(request, 'editorial/borrar_editorial.html', {'editorial': editorial})

# Vistas para Multas
def listar_multas(request):
    multas = Multa.objects.all()
    return render(request, 'multa/listar_multas.html', {'multas': multas})

def agregar_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_multas')
    else:
        form = MultaForm()
    return render(request, 'multa/agregar_multa.html', {'form': form})

def ver_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    return render(request, 'multa/ver_multa.html', {'multa': multa})

def actualizar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == 'POST':
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            form.save()
            return redirect('listar_multas')
    else:
        form = MultaForm(instance=multa)
    return render(request, 'multa/actualizar_multa.html', {'form': form})

def borrar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == 'POST':
        multa.delete()
        return redirect('listar_multas')
    return render(request, 'multa/borrar_multa.html', {'multa': multa})
