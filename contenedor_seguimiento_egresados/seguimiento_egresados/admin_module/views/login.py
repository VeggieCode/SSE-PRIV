from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url, render

from admin_module.forms import CustomAuthenticationForm
from admin_module.models import Coordinador


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return resolve_url('admin_module:home')

    def form_valid(self, form):
        # Obtener el usuario autenticado
        user = form.get_user()
        try:
            coordinator = Coordinador.objects.get(usuario=user)
        except Coordinador.DoesNotExist:
            coordinator = None
        if coordinator is None:
            form.add_error(None, 'El usuario no se encuentra registrado como coordinador')
            return self.form_invalid(form)
        # Limpiar el formulario
        self.request.session.flush()  # Limpia los datos de sesión
        self.request.session.modified = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            # Si el formulario fue enviado por POST, mostramos el mensaje de error
            context['show_alert'] = True
        return context


def logout_view(request):
    logout(request)
    return render(request, 'admin_module/login.html')
