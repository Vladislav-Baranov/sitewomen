from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_publ=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
        MODERATION = 2, 'На модерации'

    name = models.CharField(max_length=40, verbose_name='Имя')
    age = models.IntegerField()
    info = models.TextField(verbose_name='Текст статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_publ = models.IntegerField(choices=Status.choices,
                                  default=Status.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='post', verbose_name='Категория')
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='tags', verbose_name='Тэги')
    img = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Изображение')
    objects = models.Manager()
    public = PublishedManager()

# Create your models here.
    def __str__(self):
        return f"id: {self.pk}, name: {self.name}"

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['name']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Categories(models.Model):
    name = models.CharField(max_length=40, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPosts(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


