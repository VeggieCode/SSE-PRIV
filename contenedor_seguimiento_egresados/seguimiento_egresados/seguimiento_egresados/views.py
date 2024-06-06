from django.shortcuts import render


def custom_error_view(request, exception=None):
    return render(request, 'seguimiento_egresados/500.html', status=500)


def error_404_view(request, exception=None):
    response = {
        'status': 404,
        'message': 'No se encontró la página que buscaba',
    }
    return render(request, 'seguimiento_egresados/404.html', context=response)
