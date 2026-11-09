from service_objects.services import Service
from models_app.models.user.models import CustomUser
from models_app.models.post.models import Post
from django.core.paginator import Paginator
from django import forms


class MainPageService(Service):
    page = forms.IntegerField(required=False, initial=1)
    def process(self):
        user_with_photo = CustomUser.objects.filter(photo__isnull=False).distinct()
        posts_time_sort = Post.objects.order_by("-created_at")
        paginator = Paginator(posts_time_sort, 10)
        page_number = self.cleaned_data.get('page', 1)
        posts = paginator.get_page(page_number)

        return {
            'user_with_photo' : user_with_photo,
            'posts' : posts,
            'has_next': posts.has_next(),
            'next_page_number': posts.next_page_number() if posts.has_next() else None,

        }