from django.contrib import admin, messages
from .models import Women, Categories
from django.db.models.functions import Length
# Register your models here.
admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Известные женщины'

class MarriedStatus(admin.SimpleListFilter):
    title = 'Семейное положение'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(nation__is_married=1)
        elif self.value() == 'single':
            return queryset.filter(nation__is_married=0)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'info', 'slug', 'cat', 'tags', 'is_publ']
    #readonly_fields = ['slug']
    prepopulated_fields = {'slug': ('name', )}
    filter_horizontal = ['tags']
    list_display = ('name', 'time_create', 'is_publ', 'cat', 'brief_info')
    list_display_links = ('name', )
    list_editable = ('is_publ', )
    list_per_page = 10
    actions = ['set_published', 'set_draft', 'set_moderation']
    search_fields = ['name', 'cat__name']
    list_filter = [MarriedStatus, 'is_publ']

    @admin.display(description='Информация о публикации', ordering=Length("info"))
    def brief_info(self, women: Women):
        return f"Размер публикации {len(women.info)} символов"

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


