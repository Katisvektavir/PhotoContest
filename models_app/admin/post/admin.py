from django.contrib import admin
from models_app.models.post.models import Post
from models_app.models.photo.models import Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]