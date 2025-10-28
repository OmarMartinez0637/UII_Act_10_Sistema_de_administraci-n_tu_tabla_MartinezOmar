from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Página principal de la aplicación proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/anadir/', views.anadir_proveedor, name='anadir_proveedor'),
    path('proveedores/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/<int:pk>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:pk>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]