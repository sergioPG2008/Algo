from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal_view, name='principal'), # Ruta raíz
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('navbar/', views.navbar_view, name='navbar'),
    path('creadores/', views.creadores_view, name='creadores'),
    path('buscar/', views.buscar_usuario, name='search'),
    path('editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
]