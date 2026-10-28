from service_objects.services import Service
from django import forms
from django.db.models import Count
from models_app.models.post.models import Post

class PostsSortService(Service):
    sort = forms.CharField()
    def process(self):
        sort = self.cleaned_data["sort"]
        if sort == "like":
            posts = Post.objects.annotate(likes_count = Count('like')).order_by("like")
        else:
            posts = Post.objects.order_by("-created_at")
        return {"posts": posts}
