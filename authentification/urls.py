from django.urls import path
from authentification.views.login_view import LoginView
from authentification.views.logout_view import LogoutView
from authentification.views.register_view import RegisterView

app_name = 'authentification'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]