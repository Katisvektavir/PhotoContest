from service_objects.services import Service
from service_objects.fields import ModelField
from models_app.models.user.models import CustomUser
from models_app.models.post.models import Post
from models_app.models.photo.models import Photo
from django import forms

class CabinetDataService(Service):
    user = ModelField(CustomUser)

    def process(self):
        user = self.cleaned_data['user']
        posts = Post.objects.filter(user=user).order_by('-created_at')
        user_photos = Photo.objects.filter(user=user, is_avatar=False).order_by('-created_at')

        return {
            'posts': posts,
            'user_photos': user_photos,
        }

class CreatePostService(Service):
    user = ModelField(CustomUser)
    message = forms.CharField(max_length=2000)
    images = forms.FileField(required=False)

    def process(self):
        post = Post.objects.create(
            user=self.cleaned_data['user'],
            message=self.cleaned_data['message']
        )

        image = self.cleaned_data.get('images')
        if image:
            Photo.objects.create(
                user=self.cleaned_data['user'],
                post=post,
                image=image,
                is_avatar=False
            )

        return post

class UploadPhotoService(Service):
    user = ModelField(CustomUser)
    image = forms.ImageField()
    is_avatar = forms.BooleanField(required=False)

    def process(self):
        photo = Photo.objects.create(
            user=self.cleaned_data['user'],
            image=self.cleaned_data['image'],
            is_avatar=self.cleaned_data['is_avatar']
        )
        return photo