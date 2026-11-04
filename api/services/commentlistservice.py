from service_objects.services import Service
from models_app.models.comment.models import Comment
from django import forms


class CommentListService(Service):
    post_id = forms.IntegerField()
    def process(self):
        commentaries = (Comment.objects
                        .filter(post_id=self.cleaned_data['post_id'], parent_comment__isnull=True)
                        .select_related('user')
                        .prefetch_related('comments__user')
                        .order_by('-created_at'))
        return {
            'commentaries' : commentaries,
        }
