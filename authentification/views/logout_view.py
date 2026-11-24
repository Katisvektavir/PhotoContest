from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('authentification:login')