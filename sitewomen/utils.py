menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
    paginate_by = 2
    title_name = None
    extra_context = {}
    cat_selected = None
    button_name = None

    def __init__(self):
        if self.title_name:
            self.extra_context['title'] = self.title_name

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

        if 'button_name' not in self.extra_context:
            self.extra_context['button_name'] = self.button_name

    def get_mixin_context(self, context, **kwargs):
        if "paginator" in context and "page_obj" in context:
            context["page_range"] = context["paginator"].get_elided_page_range(context["page_obj"].number,
                                                                               on_each_side=1, on_ends=1)
        context['cat_selected'] = None
        context.update(kwargs)
        return context
