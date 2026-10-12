from django.views import View
from django.shortcuts import render
from models_app.models.user.models import CustomUser
from models_app.models.photo.models import Photo
from models_app.models.post.models import Post
from service.services.mainpageservice import MainPageService

class MainViews(View):
    def get(self, request):
        context = MainPageService.execute({})
        return render(request, "index.html", context)