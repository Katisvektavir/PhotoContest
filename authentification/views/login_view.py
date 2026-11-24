from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib import messages
from authentification.forms.login_form import LoginForm


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Добро пожаловать, {form.get_user().username}!")
        return response