from django.views import View
from django.shortcuts import render
from models_app.models.user.models import CustomUser
from models_app.models.photo.models import Photo

class IndexView(View):
    def get(self, request):
        user_with_photo = CustomUser.objects.filter(photo__isnull=False).distinct()
        context = {
            'user_with_photo' : user_with_photo,
        }
        return render(request, "index.html", context)