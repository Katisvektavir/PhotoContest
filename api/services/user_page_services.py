from service_objects.services import Service
from service_objects.fields import ModelField
from api.forms.post_form.forms import PostForm
from api.forms.photo_form.forms import PhotoForm
from models_app.models.user.models import CustomUser
from models_app.models.post.models import Post
from models_app.models.photo.models import Photo
from django.db import transaction, models
from django import forms
from api.utils.images import is_valid_image


class CabinetDataService(Service):
    user = ModelField(CustomUser)

    def process(self):
        user = self.cleaned_data['user']
        posts = Post.objects.filter(user=user).order_by('-created_at')
        user_photos = Photo.objects.filter(user=user, is_avatar=False).order_by('-created_at')

        return {
            'posts': posts,
            'user_photos': user_photos,
            'post_form': PostForm(),
            'photo_form': PhotoForm(),
        }


class CreatePostService(Service):
    user = ModelField(CustomUser)
    message = forms.CharField(max_length=2000)

    def clean(self):
        cleaned = super().clean()
        images = self.files.getlist('images') if self.files else []
        for image in images:
            if not is_valid_image(image):
                raise forms.ValidationError(
                    f"Файл «{getattr(image, 'name', '?')}» повреждён "
                    f"или не является изображением. Пост не создан."
                )
        self._images = images
        return cleaned

    @transaction.atomic
    def process(self):
        post = Post.objects.create(
            user=self.cleaned_data['user'],
            message=self.cleaned_data['message']
        )
        for image in self._images:
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

    def clean_image(self):
        image = self.cleaned_data['image']
        if not is_valid_image(image):
            raise forms.ValidationError(
                "Файл повреждён или загружен не полностью. Попробуйте ещё раз."
            )
        return image

    def process(self):

        photo = Photo.objects.create(
            user=self.cleaned_data['user'],
            image=self.cleaned_data['image'],
            is_avatar=self.cleaned_data['is_avatar']
        )
        return photo