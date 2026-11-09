from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from api.services.user_page_services import CabinetDataService, CreatePostService, UploadPhotoService


class UserPageView(LoginRequiredMixin, View):
    template_name = 'user_page.html'

    def get(self, request):
        # Получаем данные для всех вкладок через сервис
        context = CabinetDataService.execute({'user': request.user})
        return render(request, self.template_name, context)

    def post(self, request):
        # Определяем, какую форму отправил пользователь (по name кнопки)
        if 'create_post' in request.POST:
            service = CreatePostService({
                'user': request.user,
                'message': request.POST.get('message'),
                'images': request.FILES.getlist('images')  # Если фото несколько
            })
            if service.is_valid():
                service.process()
                messages.success(request, "Пост успешно создан и отправлен на модерацию!")
                return redirect('cabinet')
            else:
                messages.error(request, "Ошибка при создании поста. Проверьте данные.")

        elif 'upload_photo' in request.POST:
            service = UploadPhotoService({
                'user': request.user,
                'image': request.FILES.get('image'),
                'is_avatar': request.POST.get('is_avatar') == 'on'
            })
            if service.is_valid():
                service.process()
                messages.success(request, "Фото загружено!")
                return redirect('cabinet')
            else:
                messages.error(request, "Ошибка при загрузке фото.")

        # Если форма невалидна — рендерим страницу заново (с ошибками)
        context = CabinetDataService.execute({'user': request.user})
        return render(request, self.template_name, context)