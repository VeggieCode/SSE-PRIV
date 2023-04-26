from django.shortcuts import render 

def custom_error_view(request, exception=None):
    return render(request, '500.html', status=500)