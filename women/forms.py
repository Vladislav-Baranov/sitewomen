from django import forms
from .models import Categories, Women

IS_PUBLISHED_FORM = ([0, 'Черновик'],
 [1, 'Опубликовано'],
 [2, 'На модерации'], )


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    slug = forms.SlugField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    is_publ = forms.IntegerField(widget=forms.Select(choices=IS_PUBLISHED_FORM))
    cat = forms.ModelChoiceField(queryset=Categories.objects.all())
