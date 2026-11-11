from django import forms
from models_app.models.post.models import Post
from models_app.models.photo.models import Photo

class PostForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        required=False,
        label="Фотографии (можно несколько)"
    )

    class Meta:
        model = Post
        fields = ['message'] # Берем только текстовое поле из модели
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'О чем ваш пост?'
            }),
        }
        labels = {
            'message': 'Текст поста'
        }
