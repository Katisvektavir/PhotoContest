from django.views import View
from authentification.forms.login_form import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from authentification.services.login_service import LoginService


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form" : form})

    def post(self, request):
        service = LoginService({
            'username': request.POST.get('username', ''),
            'password': request.POST.get('password', ''),
        })

        if service.is_valid():
            user = service.process()
            login(request, user)
            return redirect('/')
        form = LoginForm(data=request.POST)
        for err in service.errors.get('__all__', []):
           form.add_error(None, err)
        return render(request, self.template_name, {"form" : form})
