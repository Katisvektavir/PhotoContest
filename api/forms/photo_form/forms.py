from django import forms
from models_app.models.post.models import Post
from models_app.models.photo.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'is_avatar']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_avatar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'image': 'Выберите картинку',
            'is_avatar': 'Сделать аватаркой'
        }