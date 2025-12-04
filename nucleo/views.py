from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Client

def login_view(request):
    if request.method == 'POST':
        try:
            v_nombre = request.POST['nombre']
            v_apellidos = request.POST['apellidos']
            v_telefono = request.POST['telefono']
            v_gmail = request.POST['gmail']       # <-- corregido
            v_direccion = request.POST['direccion']
            v_plantaFav = request.POST['plantaFav']

            cliente_nuevo = Client(
                nombre=v_nombre,
                apellidos=v_apellidos,
                telefono=v_telefono,
                gmail=v_gmail,
                direccion=v_direccion,
                plantaFav=v_plantaFav
            )
            cliente_nuevo.save()

            return render(request, 'login.html', {
                'mensaje': '¡Cliente registrado con éxito en la Planta BD!'
            })
        except Exception as e:
            return render(request, 'login.html', {
                'mensaje': f'Error al guardar: {e}'
            })

    return render(request, 'login.html')


def creadores_view(request):
    return render(request, 'creadores.html')

def principal_view(request):
    return render(request, 'principal.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def navbar_view(request):
    return render(request, 'navbar.html')

def buscar_usuario(request):
    # Definimos una lista vacía para evitar errores si no hay búsqueda
    resultados = [] 
    query = request.GET.get('query') # Obtenemos el texto del input

    # Si el usuario escribió algo...
    if query:
        # Aquí ocurre la MAGIA del "OR"
        # Buscamos: (Nombre contiene texto) O (Teléfono contiene texto)
        resultados = Client.objects.filter(
            Q(nombre__icontains=query) | Q(telefono__icontains=query)
        )
    
    # Enviamos los resultados al HTML
    return render(request, 'search.html', {'resultados': resultados, 'query': query})

def editar_cliente(request, id_cliente):
    # 1. BUSCAR: Obtenemos el cliente específico o mostramos error 404 si no existe
    cliente_a_editar = get_object_or_404(Client, id=id_cliente)

    # 2. PROCESAR GUARDADO (POST)
    if request.method == 'POST':
        # Actualizamos los campos del objeto con los nuevos datos del formulario
        cliente_a_editar.nombre = request.POST['nombre']
        cliente_a_editar.apellidos = request.POST['apellidos']
        cliente_a_editar.telefono = request.POST['telefono']
        cliente_a_editar.gmail = request.POST['gmail']
        cliente_a_editar.direccion = request.POST['direccion']
        cliente_a_editar.plantaFav = request.POST['plantaFav']

        # Guardamos los cambios en la BD (UPDATE)
        cliente_a_editar.save()

        # Redirigimos al buscador o mostramos mensaje de éxito
        return render(request, 'editar.html', {
            'cliente': cliente_a_editar,
            'mensaje': '¡Datos actualizados correctamente!'
        })

    # 3. CARGAR FORMULARIO (GET)
    # Si apenas entramos a la página, le enviamos los datos actuales del cliente
    # para que el HTML pueda rellenar los inputs.
    return render(request, 'editar.html', {'cliente': cliente_a_editar})

def eliminar_cliente(request, id_cliente):
    cliente_a_borrar = get_object_or_404(Client, id=id_cliente)

    if request.method == 'POST':
        cliente_a_borrar.delete()
        return redirect('/buscar/')  # ✅ usa la ruta o el name correcto

    return render(request, 'eliminar_confirmar.html', {'cliente': cliente_a_borrar})