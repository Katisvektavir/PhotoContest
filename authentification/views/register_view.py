from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from authentification.forms.register_form import RegisterForm


class RegisterView(View):
    template_name = "register.html"
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form" : form})
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})