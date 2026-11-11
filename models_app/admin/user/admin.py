from django.contrib import admin
from models_app.models.user.models import CustomUser

admin.site.register(CustomUser)