from django.http import JsonResponse
from api.services.like_toggle_service import ToggleLikeService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from api.services.comment_add_service import CommentAddService
from django.template.loader import render_to_string
from models_app.models.post.models import Post



class CommentCreateView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return JsonResponse({'error': 'auth required'}, status=401)

    def post(self, request, post_id):
        service = CommentAddService({
            'post_id': post_id,
            'user': request.user,
            'message': request.POST.get('message', '').strip(),
            'parent_id': request.POST.get('parent_id') or None,
        })
        if not service.is_valid():
            return JsonResponse({'errors': service.errors}, status=400)

        result = service.process()
        html = render_to_string('comment_list.html', {'commentaries': result['commentaries'], 'post': result['post']},request=request,)
        return JsonResponse({'html': html, 'comments_count': result['post'].comments.count(),})