from django.views import View
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from models_app.models.user.models import CustomUser
from models_app.models.photo.models import Photo
from models_app.models.post.models import Post
from api.services.mainpageservice import MainPageService


class MainViews(View):
    def get(self, request):
        page_number = request.GET.get('page', 1)
        context = MainPageService.execute({
            'page': page_number,
            'user': request.user
        })
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            html = render_to_string('posts_list.html', context, request=request)
            return JsonResponse({
                'html': html,
                'has_next': context['has_next'],
                'next_page_number': context['next_page_number']
            })

        return render(request, "index.html", context)