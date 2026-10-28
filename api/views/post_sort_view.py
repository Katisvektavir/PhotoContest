from django.views import View
from django.shortcuts import render
from models_app.models.user.models import CustomUser
from models_app.models.photo.models import Photo
from models_app.models.post.models import Post
from api.services.postsortservice import PostsSortService

class PostsSortView(View):
    def get(self, request):
        sort = request.GET.get("sort", "date")
        context = PostsSortService.execute({"sort": sort})
        return render(request, "posts_list.html", context)
