from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from veterinariaApp.forms import CitaMedicaForm, MascotaForm, TratamientoForm, DueñoForm
from veterinariaApp.models import CitaMedica, Mascota, Tratamiento, Dueño

# Create your views here.

def inicio(request):
    return render(request,'index.html')
###     Cita Medica     ###
def menuCita(request):
    return render(request, 'CitaMedica/Cita.html')
def crearMedica(request):
    return render(request, 'CitaMedica/CrearCita.html')

def listarCita(request):
    return render(request, 'CitaMedica/MostrarCita.html')

def editarCita(request):
    return render(request, 'CitaMedica/EditarCita.html')

###     Dueño       ###
def menuDueño(request):
    dueños = Dueño.objects.all()  
    return render(request, 'dueño/Dueño.html', {'dueños': dueños})
def crearDueño(request):
    return render(request, 'dueño/Crear.html')

def listarDueño(request):
    return render(request, 'dueño/mostrar.html')

def editarDueño(request):
    return render(request, 'dueño/editar.html')


###     Mascota     ###
def menuMascota(request):
    return render(request, 'mascota/Mascota.html')
def crearMascota(request):
    return render(request, 'mascota/CrearMascota.html')

def listarMascota(request):
    return render(request, 'mascota/mostrarMascota.html')

def editarMascota(request):
    return render(request, 'mascota/EditarMascota.html')

###     Tratamiento     ###
def menuTratamientos(request):
    return render(request, 'Tratamiento/Tratamiento.html')
def crearTratamiento(request):
    return render(request, 'Tratamiento/CrearTratamiento.html')

def listarTratamiento(request):
    return render(request, 'Tratamiento/MostrarTratamiento.html')

def editarTratamiento(request):
    return render(request, 'Tratamiento/EditarTratamiento.html')

# Vista de menú de dueño
def menuDueño(request):
    return render(request, 'dueño/Dueño.html')


def crearDueño(request):
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MostrarDueño')
    else:
        form = DueñoForm()
    return render(request, 'dueño/Crear.html', {'form': form})


def listarDueño(request):

    dueños = Dueño.objects.all()

    print(dueños)

    return render(request, 'dueño/mostrar.html', {'dueños': dueños})


def editarDueño(request, id):
    dueño = get_object_or_404(Dueño, id=id)
    if request.method == 'POST':
        form = DueñoForm(request.POST, instance=dueño)
        if form.is_valid():
            form.save()
            return redirect('MostrarDueño')
    else:
        form = DueñoForm(instance=dueño)
    return render(request, 'dueño/editar.html', {'form': form, 'dueño': dueño})

def eliminarDueño(request, id):
    dueño = get_object_or_404(Dueño, id=id)
    dueño.delete()
    return redirect('MostrarDueño')

###   Mascota   ###

def crearMascota(request):
    form = MascotaForm()
    data = {
        'Titulo': 'Crear Mascota',
        'Formulario': form
    }
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, 'La mascota ha sido registrada con éxito')
            return redirect('MostrarMascota')
    return render(request, 'mascota/CrearMascota.html', data)

def listarMascota(request):
    mascota = Mascota.objects.all()
    data = {'lista': mascota}
    return render(request, 'mascota/mostrarMascota.html', data)

def editarMascota(request, id):
    mascota = Mascota.objects.get(pk=id)
    form = MascotaForm(instance=mascota)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'La mascota ha sido editada')
            return redirect('MostrarMascota')  
    data = {
        'Titulo': 'Editar Mascota',
        'Formulario': form
    }
    return render(request, 'mascota/EditarMascota.html', data)

def eliminarMascota(request, id):
    mascota = Mascota.objects.get(pk=id)
    mascota.delete()
    messages.success(request, 'La mascota ha sido eliminada')
    return redirect('MostrarMascota')  


###     Cita Medica     ###
def crearMedica(request):
    form = CitaMedicaForm()
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita médica ha sido creada con éxito')
            return redirect('MostrarCita')  
        else:
            messages.error(request, 'Hubo un error al crear la cita médica. Por favor, revisa los campos.')
    return render(request, 'CitaMedica/CrearCita.html', {'Titulo': 'Crear Cita Médica', 'Formulario': form})
def listarCita(request):
    citas = CitaMedica.objects.all()  
    data = {'lista': citas}
    return render(request, 'CitaMedica/MostrarCita.html', data)

def editarCita(request, id):
    cita = CitaMedica.objects.get(pk=id)
    form = CitaMedicaForm(instance=cita)
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita se ha editado con éxito')
            return redirect('MostrarCita')  
    data = {
        'Titulo': 'Editar Cita Médica',
        'Formulario': form
    }
    return render(request, 'CitaMedica/EditarCita.html', data)

def eliminarCita(request, id):
    cita = CitaMedica.objects.get(pk=id)
    cita.delete()
    messages.success(request, 'La cita médica ha sido eliminada con éxito')
    return redirect('MostrarCita')  

###     Tratamiento     ###

def crearTratamiento(request):
    form = TratamientoForm()
    data = {
        'Titulo': 'Crear Tratamiento',
        'Formulario': form
    }
    if request.method == 'POST':
        form = TratamientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento creado con éxito')
            return redirect('MostrarTratamiento')
        else:
            print(form.errors) 
    return render(request, 'Tratamiento/CrearTratamiento.html', data)

def listarTratamiento(request):
    tratamiento = Tratamiento.objects.all()
    data = {'lista': tratamiento}
    return render(request, 'Tratamiento/MostrarTratamiento.html', data)

def editarTratamiento(request, id):
    tratamiento = Tratamiento.objects.get(pk=id)
    form = TratamientoForm(instance=tratamiento)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, request.FILES, instance=tratamiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento actualizado con éxito')
            return redirect('MostrarTratamiento')
    data = {
        'Titulo': 'Editar Tratamiento',
        'Formulario': form
    }
    return render(request, 'Tratamiento/EditarTratamiento.html', data)

def eliminarTratamiento(request, id):
    tratamiento = Tratamiento.objects.get(pk=id)
    tratamiento.delete()
    messages.success(request, 'Tratamiento eliminado con éxito')
    return redirect('MostrarTratamiento')