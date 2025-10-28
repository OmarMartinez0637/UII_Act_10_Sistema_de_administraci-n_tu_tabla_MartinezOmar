from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

# Vista para la página principal (home)
def home(request):
    return render(request, 'proveedores/home.html')

# Vista para listar todos los proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

# Vista para ver los detalles de un proveedor específico
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk) # Obtiene el proveedor o devuelve un 404
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})

# Vista para añadir un nuevo proveedor
def anadir_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores') # Redirige a la lista después de guardar
    else:
        form = ProveedorForm() # Formulario vacío para GET
    return render(request, 'proveedores/anadir_proveedor.html', {'form': form})

# Vista para editar un proveedor existente
# ... (otras importaciones)

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    # Asegúrate de pasar 'proveedor' explícitamente al contexto de la plantilla
    return render(request, 'proveedores/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

# Vista para eliminar un proveedor
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST': # Solo elimina si la petición es POST (confirmación)
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'proveedores/confirmar_eliminar_proveedor.html', {'proveedor': proveedor})