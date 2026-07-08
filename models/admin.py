from django.contrib import admin
from models.models import CustomUser, Photo, Like, Comment, Post
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Photo)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)