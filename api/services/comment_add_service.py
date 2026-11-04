from django import forms
from django.shortcuts import get_object_or_404
from service_objects.services import Service
from service_objects.fields import ModelField
from models_app.models.post.models import Post
from models_app.models.comment.models import Comment
from models_app.models.user.models import CustomUser


class CommentAddService(Service):
    post_id = forms.IntegerField()
    user = ModelField(CustomUser)
    message = forms.CharField(max_length=2000)
    parent_id = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        parent_id = cleaned_data.get('parent_id')
        post_id = cleaned_data.get('post_id')

        if parent_id and post_id:
            if parent_id and post_id:
                parent = Comment.objects.filter(id=parent_id, post_id=post_id).first()
                if not parent:
                    raise forms.ValidationError('Родительский комментарий не найден')
                if parent.parent_comment_id is not None:
                    raise forms.ValidationError('Максимум 2 уровня вложенности')
                cleaned_data['parent'] = parent
            return cleaned_data

    def process(self):
        post = get_object_or_404(Post, id=self.cleaned_data['post_id'])

        Comment.objects.create(
            post=post,
            user=self.cleaned_data['user'],
            message=self.cleaned_data['message'],
            parent_comment=self.cleaned_data.get('parent'),
        )

        commentaries = (Comment.objects
                        .filter(post_id=self.cleaned_data['post_id'], parent_comment__isnull=True)
                        .select_related('user')
                        .prefetch_related('comments__user')
                        .order_by('-created_at'))

        return {'commentaries': commentaries, 'post': post}