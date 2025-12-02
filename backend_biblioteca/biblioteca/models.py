from django.db import models

# Tabla Autor_Biblioteca
class Autor(models.Model):
    nombre_autor = models.CharField(max_length=100)
    apellido_autor = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    libros_destacados = models.TextField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Autor_Biblioteca'

    def __str__(self):
        return f"{self.nombre_autor} {self.apellido_autor}"

# Tabla Editorial_Biblioteca
class Editorial(models.Model):
    nombre_editorial = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    sitio_web = models.URLField(max_length=255)
    fecha_fundacion = models.DateField()

    class Meta:
        db_table = 'Editorial_Biblioteca'

    def __str__(self):
        return self.nombre_editorial

# Tabla Socio
class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField()
    fecha_vencimiento_membresia = models.DateField()
    dni = models.CharField(max_length=20)
    tipo_socio = models.CharField(max_length=50)

    class Meta:
        db_table = 'Socio'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla Bibliotecario
class Bibliotecario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    turno = models.CharField(max_length=50)

    class Meta:
        db_table = 'Bibliotecario'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla Libro_Biblioteca
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, to_field='nombre_editorial')
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)
    num_ejemplares = models.IntegerField()
    fecha_adquisicion = models.DateField()
    estanteria = models.CharField(max_length=50)

    class Meta:
        db_table = 'Libro_Biblioteca'

    def __str__(self):
        return self.titulo

# Tabla Prestamo
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateTimeField(null=True, blank=True)
    estado_prestamo = models.CharField(max_length=50)
    multa_generada = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'Prestamo'

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.socio.nombre}"

# Tabla Multa
class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto_multa = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_generacion = models.DateTimeField()
    fecha_pago = models.DateTimeField(null=True, blank=True)
    estado_pago = models.CharField(max_length=50)
    motivo_multa = models.TextField()
    socio_multado = models.ForeignKey(Socio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Multa'

    def __str__(self):
        return f"Multa para {self.socio_multado.nombre} por ${self.monto_multa}"
