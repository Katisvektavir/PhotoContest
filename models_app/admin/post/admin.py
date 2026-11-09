from django.contrib import admin
from .models.post.models import Post
from .models.photo.models import Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]