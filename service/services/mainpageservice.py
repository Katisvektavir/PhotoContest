from service_objects.services import Service
from models_app.models.user.models import CustomUser
from models_app.models.post.models import Post

class MainPageService(Service):
    def process(self):
        user_with_photo = CustomUser.objects.filter(photo__isnull=False).distinct()
        posts_time_sort = Post.objects.order_by("-created_at")

        return {
            'user_with_photo' : user_with_photo,
            'posts' : posts_time_sort,
        }