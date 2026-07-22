from django.contrib import admin
from models_app.post.models import Post
from models_app.comment.models import Comment
from models_app.user.models import CustomUser
from models_app.photo.models import Photo
from models_app.like.models import Like
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Photo)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)