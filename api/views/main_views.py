from django.views import View
from django.shortcuts import render
from models_app.models.user.models import CustomUser
from models_app.models.photo.models import Photo
from models_app.models.post.models import Post


class MainViews(View):
    def get(self, request):
        user_with_photo = CustomUser.objects.filter(photo__isnull=False).distinct()
        posts_time_sort = Post.objects.order_by("-created_at")
        context = {
            'user_with_photo' : user_with_photo,
            'posts_time_sort' : posts_time_sort,
        }
        return render(request, "index.html", context)