from service_objects.services import Service
from models_app.models.post.models import Post
from models_app.models.like.models import Like
from models_app.models.comment.models import Comment
from models_app.models.user.models import CustomUser
from django.shortcuts import get_object_or_404
from service_objects.fields import ModelField
from django import forms

class ToggleLikeService(Service):
    comment_id = forms.IntegerField(required=False)
    user = ModelField(CustomUser)
    post_id = forms.IntegerField(required=False)
    def process(self):
        user = self.cleaned_data['user']
        post_id = self.cleaned_data.get('post_id')
        comment_id = self.cleaned_data.get('comment_id')
        if post_id:
            post = get_object_or_404(
                Post,
                id=self.cleaned_data['post_id'],
            )
            like, created = Like.objects.get_or_create(user=self.cleaned_data['user'], post=post)
            target = post
        else:
            comment = get_object_or_404(
                Comment,
                id=comment_id
            )
            like, created = Like.objects.get_or_create(user=user, comment=comment)
            target = comment
        if not created:
            like.delete()

        return {
            'liked': created,
            'likes_count': target.likes.count(),
        }