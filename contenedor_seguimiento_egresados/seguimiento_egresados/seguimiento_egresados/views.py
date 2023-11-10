from django.shortcuts import render

def custom_error_view(request, exception=None):
    return render(request, '500.html', status=500)
def error_404_view(request, exception):
    response = {
        'status': 404,
        'message': 'No se encontró la página que buscaba',
    }
    return render(request, template_name='404.html', context=response)