from django import template
import women.views as views
from women.models import Categories, TagPosts
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Categories.objects.annotate(total=Count('post')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected_id}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": TagPosts.objects.annotate(total=Count('tags')).filter(total__gt=0)}
