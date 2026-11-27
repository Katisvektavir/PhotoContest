from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('authentification:login')

    def get(self, request):
        return redirect('authentification:login')