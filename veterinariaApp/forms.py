from django import forms
from .models import Dueño, Mascota, CitaMedica, Tratamiento

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ['nombre', 'rut', 'direccion', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del dueño'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'edad', 'tipo', 'foto', 'dueño']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo (e.g., Perro, Gato)'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'dueño': forms.Select(attrs={'class': 'form-control'}),
        }

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['mascota', 'veterinario', 'fecha', 'hora', 'descripcion']
        widgets = {
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'veterinario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del veterinario'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la cita', 'rows': 3}),
        }

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['cita', 'medicamentos', 'instrucciones', 'archivo_adjunto']
        widgets = {
            'cita': forms.Select(attrs={'class': 'form-control'}),
            'medicamentos': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Medicamentos prescritos', 'rows': 3}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instrucciones para el tratamiento', 'rows': 3}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
