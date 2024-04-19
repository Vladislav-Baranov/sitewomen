from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Categories
from django.db.models.functions import Length
# Register your models here.
admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Известные женщины'


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'info', 'slug', 'cat', 'tags', 'is_publ', 'img', 'post_photo']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('name', )}
    filter_horizontal = ['tags']
    list_display = ('name', 'time_create', 'is_publ', 'cat', 'post_photo')
    list_display_links = ('name', )
    list_editable = ('is_publ', )
    list_per_page = 10
    actions = ['set_published', 'set_draft', 'set_moderation']
    search_fields = ['name', 'cat__name']
    list_filter = ['is_publ']
    save_on_top = True

    @admin.display(description='Фото')
    def post_photo(self, women: Women):
        if women.img:
            return mark_safe(f"<img src='{women.img.url}' alt='' width=100 high=100>")
        else:
            return "Без фото"


    @admin.action(description='Опубликовать записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_publ=Women.Status.PUBLISHED)
        self.message_user(request, f'Опубликовано {count} записей')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_publ=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации', messages.WARNING)

    @admin.action(description='Отправить на модерацию')
    def set_moderation(self, request, queryset):
        count = queryset.update(is_publ=Women.Status.MODERATION)
        self.message_user(request, f'{count} записей отправлено на модерацию')
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


