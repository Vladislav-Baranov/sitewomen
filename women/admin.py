from django.contrib import admin
from .models import Women
# Register your models here.
admin.site.register(Women)
admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Известные женщины'

