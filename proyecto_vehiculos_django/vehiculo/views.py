from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vehiculo
from django.contrib.auth.decorators import login_required
# Create your views here.

def firts_view(request):
    return render(request,'index.html')

@login_required
def lista(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista.html', {'vehiculos': vehiculos})

def login(request):
    return render(request, 'login.html')


def enviar(request):

    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        serial_carroceria = request.POST['serial_carroceria']
        serial_motor = request.POST['serial_motor']
        categoria = request.POST['categoria']
        precio = int(request.POST['precio'])
        if precio <= 0:
            messages.error(request, 'El precio debe ser mayor a cero.')
        else:
            vehiculo = Vehiculo.objects.create(
                marca=marca,
                modelo=modelo,
                serial_carroceria=serial_carroceria,
                serial_motor=serial_motor,
                categoria=categoria,
                precio=precio
            )
            messages.success(request, 'Vehículo agregado exitosamente.')
        return redirect('enviar')
    return render(request,'enviar.html')





















# def enviar(request):
#     if request.method == 'POST':
#         marca = request.POST['marca']
#         modelo = request.POST['modelo']
#         serial_carroceria = request.POST['serial_carroceria']
#         serial_motor = request.POST['serial_motor']
#         categoria = request.POST['categoria']
#         precio = int(request.POST['precio'])
        
            
#     else:
#         form = Vehiculo()
#     return render(request, 'enviar.html') 



    # return render(request,'enviar.html')