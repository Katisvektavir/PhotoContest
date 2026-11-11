from django.http import JsonResponse
from api.services.like_toggle_service import ToggleLikeService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class PostLikeView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return JsonResponse({'error': 'auth required'}, status=401)

    def post(self, request, post_id):
        result = ToggleLikeService.execute({
            'post_id': post_id,
            'user': request.user
        })
        return JsonResponse(result)

class CommentLikeView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return JsonResponse({'error': 'auth required'}, status=401)

    def post(self, request, comment_id):
        result = ToggleLikeService.execute({
            'user': request.user,
            'comment_id': comment_id,
        })
        return JsonResponse(result)