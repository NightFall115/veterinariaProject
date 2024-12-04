from django.db import models

# Create your models here.
class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} ({self.rut})'
    
    class Meta:
        db_table = 'Dueño'

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)  
    dueño = models.ForeignKey('Dueño', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
        
class CitaMedica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f'Cita para {self.mascota.nombre} en {self.fecha} a las {self.hora}'
        
class Tratamiento(models.Model):
    cita = models.OneToOneField(CitaMedica, on_delete=models.CASCADE)
    medicamentos = models.TextField()
    instrucciones = models.TextField()
    archivo_adjunto = models.FileField(upload_to='tratamientos/', blank=True, null=True)

    def __str__(self):
        return f'Tratamiento para {self.cita.mascota.nombre} ({self.cita.fecha})'

    class Meta:
        db_table = 'Tratamiento'