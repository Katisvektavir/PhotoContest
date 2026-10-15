from django.views import View
from django.shortcuts import render
from models_app.models.post.models import Post
from service.services.commentlistservice import CommentListService

class CommentListView(View):
    def get(self, request, post_id):
        context = CommentListService.execute({"post_id": post_id})
        return render(request, "comment_list.html", context)
