from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from models_app.models.photo.models import Photo
from api.services.user_page_services import CabinetDataService, CreatePostService, UploadPhotoService
from api.utils.images import is_valid_image



class UserPageView(LoginRequiredMixin, View):
    template_name = 'user_page.html'

    def get(self, request):
        context = CabinetDataService.execute({'user': request.user})
        return render(request, self.template_name, context)

    def post(self, request):
        if 'create_post' in request.POST:
            post = CreatePostService.execute({
                'user': request.user,
                'message': request.POST.get('message', '').strip(),
            })

            if post:
                images = request.FILES.getlist('images')
                skipped = 0

                for img in images:
                    if not is_valid_image(img):
                        skipped += 1
                        continue

                    Photo.objects.create(
                        user=request.user,
                        post=post,
                        image=img,
                        is_avatar=False
                    )
                if skipped:
                    messages.warning(
                        request,
                        f"{skipped} файл(ов) не сохранено: повреждены. "
                        f"Попробуйте загрузить их снова."
                    )
                messages.success(request, "Пост успешно создан и отправлен на модерацию!")
                return redirect('/user')
            else:
                messages.error(request, "Ошибка при создании поста. Проверьте данные.")

        elif 'upload_photo' in request.POST:
            service = UploadPhotoService(
                data = {
                'user': request.user,
                'is_avatar': request.POST.get('is_avatar') == 'on',
                },
                files = {
                    'image': request.FILES.get('image'),
                },
            )
            if service.is_valid():
                service.process()
                messages.success(request, "Фото загружено!")
                return redirect('/user')
            else:
                messages.error(request, "Ошибка при загрузке фото.")

        context = CabinetDataService.execute({'user': request.user})
        return render(request, self.template_name, context)