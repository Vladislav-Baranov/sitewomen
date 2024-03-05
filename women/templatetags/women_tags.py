from django import template
import women.views as views
from women.models import Categories

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected_id}
