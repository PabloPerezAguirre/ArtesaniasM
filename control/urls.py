from django.urls import path
from control.views import producto, produccion, material, produccion_editar, producto_eliminar, producto_editar, produccion_eliminar, material_editar, material_eliminar, ver_material, ver_produccion, ver_producto

urlpatterns = [
    path('producto/', producto, name= 'control-producto'),
    path('producto/ver/<int:pk>/', ver_producto, name= 'control-verproducto'),
    path('producto/editar/<int:pk>/', producto_editar, name='control-producto-editar'),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name='control-producto-eliminar'),
    path('produccion/', produccion, name= 'control-produccion'),
    path('produccion/ver/<int:pk>/', ver_produccion, name= 'control-verproduccion'),
    path('produccion/editar/<int:pk>/', produccion_editar, name='control-produccion-editar'),
    path('produccion/eliminar/<int:pk>/', produccion_eliminar, name='control-produccion-eliminar'),
    path('material/', material, name= 'control-material'),
    path('material/ver/<int:pk>/', ver_material, name= 'control-vermaterial'),
    path('material/editar/<int:pk>/', material_editar, name='control-material-editar'),
    path('material/eliminar/<int:pk>/', material_eliminar, name='control-material-eliminar'),
]