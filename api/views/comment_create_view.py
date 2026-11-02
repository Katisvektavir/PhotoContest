from django.http import JsonResponse
from api.services.like_toggle_service import ToggleLikeService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        result = ToggleLikeService.execute(
            {'post_id': post_id,  'user': request.user})
        print("lol lol ", result, " lol lol")
        return JsonResponse(result)