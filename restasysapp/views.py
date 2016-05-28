from django.shortcuts import render
from .models import Mesa, Pratos, Pedidos, Pedidos_Fechados
from .forms import MesaForm, PratosForm, PedidosForm


def index(request):
    return render(request, 'restasysapp/home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'restasysapp/cliente_list.html', {'clientes':clientes})

def mesa_novo(request):
    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            mesa = form.save()
            form = MesaForm()
    else:
        form = MesaForm()
    return render(request, 'restasysapp/mesa_novo.html', {'form': form})

def prato_novo(request):
    if request.method == "POST":
        form = PratosForm(request.POST)
        if form.is_valid():
            pratos = form.save()
            form = PratosForm()
    else:
        form = PratosForm()
    return render(request, 'restasysapp/prato_novo.html', {'form': form})

def pedido_novo(request):
    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            pedidos = form.save()
            form = PedidosForm()
    else:
        form = PedidosForm()
    return render(request, 'restasysapp/pedido_novo.html', {'form': form})
