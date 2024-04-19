from django import forms
from django.core.exceptions import ValidationError

from .models import Categories, Women, TagPosts
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible


class AddPostForm(forms.ModelForm):

    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория', empty_label='Не выбрана')
    tags = forms.ModelMultipleChoiceField(queryset=TagPosts.objects.all(), label='Тэги',
                                          widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Women
        fields = ['name', 'age', 'slug', 'info', 'is_publ', 'cat', 'tags', 'img']
        labels = {'slug': 'URL'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    # def clean_info(self):
    #     info = self.cleaned_data['info']
    #     ALLOWED_CHARS = '''АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789()-,:!?—"«»'.- '''
    #     if not (set(info) <= set(ALLOWED_CHARS)):
    #         raise ValidationError("Должны быть только русские символы, дефис и пробел.")
    #     return info
