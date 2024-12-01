from django.shortcuts import redirect, render
from django.contrib import messages
from veterinariaApp.forms import CitaMedicaForm, MascotaForm, TratamientoForm, DueñoForm
from veterinariaApp.models import CitaMedica, Mascota, Tratamiento, Dueño

# Create your views here.

def inicio(request):
    return render(request,'index.html')


def crearDueño(request):
    form = DueñoForm()
    data = {
        'Titulo':'Crear Dueño',
        'Formulario':form
    }
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.succes(request,'El dueño ha sido registrado con exito')
    return render(request,'dueño/Crear.html',data)

def listarDueño(request):
    dueño = Dueño.objects.all()
    data = {'lista': dueño}

    return render(request,'dueño/mostrar.html',data)

def editarDueño(request,id):
    dueño = Dueño.objects.get(pk =id)
    form = DueñoForm(instance=dueño)
    if request.method == 'POST':
        form = DueñoForm(request.POST, instance=dueño)
        if form.is_valid():
            form.save()
            messages.success(request,'El Dueño fue modificado')
    data = {
        'Titulo':'Editar Dueño',
        'Formulario' : form
    }
    return render(request,'dueño/editar.html',data)

def eliminarDueño(request,id):
    dueño = Dueño.objects.get(pk=id)
    dueño.delete()
    return redirect('/dueño/editar.html')

###   Mascota   ###

def crearMascota(request):
    form = MascotaForm()
    data = {
        'Titulo':'Crear Mascota',
        'Formulario':form
    }
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.succes(request,'La mascota ha sido registrado con exito')
    return render(request,'mascota/CrearMascota.html',data)

def listarMascota(request):
    mascota = Mascota.objects.all()
    data = {'lista': mascota}

    return render(request,'mascota/mostrarMascota.html',data)

def editarMascota(request,id):
    mascota= Mascota.objects.get(pk = id)
    form = MascotaForm(instance=mascota)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request,'La mascota ha sido editada')
    data = {
        'Titulo':'Editar Dueño',
        'Formulario' : form
    }
    return render(request,'mascota/EditarMascota.html',data)

def eliminarMascota(request,id):
    mascota = Mascota.objects.get(pk=id)
    mascota.delete()
    return redirect('/mascota/EditarMascota.html')


###     Cita Medica     ###

def crearMedica(request):
    form = CitaMedicaForm()
    data = {
        'Titulo':'Crear Cita',
        'Formulario':form
    }
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.succes(request,'La cita medica ha sido creada con exito')
    return render(request,'CitaMedica/CrearCita.html',data)

def listarCita(request):
    cita = CitaMedica.objects.all()
    data = {'lista': cita}

    return render(request,'CitaMedica/MostrarCita.html',data)

def editarCita(request,id):
    cita= CitaMedica.objects.get(pk = id)
    form = CitaMedicaForm(instance=cita)
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request,'La cita se ha editado con exito ')
    data = {
        'Titulo':'Editar Cita',
        'Formulario' : form
    }
    return render(request,'CitaMedita/EditarCita.html',data)

def eliminarCita(request,id):
    cita = CitaMedica.objects.get(pk=id)
    cita.delete()
    return redirect('/CitaMedica/EditarCita.html')

###     Tratamiento     ###

def crearTratamiento(request):
    form = TratamientoForm()
    data = {
        'Titulo':'Crear Tratamiento',
        'Formulario':form
    }
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.succes(request,'Tratamiento ha sido creado con exito')
    return render(request,'Tratamiento/CrearTratamiento.html',data)

def listarTratamiento(request):
    tratamiento =Tratamiento.objects.all()
    data = {'lista': tratamiento}

    return render(request,'Tratamiento/MostrarTratamiento.html',data)

def editarTratamiento(request,id):
    tratamiento= Tratamiento.objects.get(pk = id)
    form = TratamientoForm(instance=tratamiento)
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            messages.success(request,'El tratamiento se ha editado con exito ')
    data = {
        'Titulo':'Editar Tratamiento',
        'Formulario' : form
    }
    return render(request,'Tratamiento/EditarTratamiento.html',data)

def eliminarTratamiento(request,id):
    tratamiento = Tratamiento.objects.get(pk=id)
    tratamiento.delete()
    return redirect('/Tratamiento/EditarTratamiento.html')