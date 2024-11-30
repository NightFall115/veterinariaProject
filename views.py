from django.shortcuts import redirect, render
from django.contrib import messages
from veterinariaApp.forms import DueñoForm
from veterinariaApp.models import Dueño

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
    dueño = Dueño.objects.get(pk.id)
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
    return redirect('/dueño/editar.html',)