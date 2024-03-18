from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_publ=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=40)
    age = models.IntegerField()
    info = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publ = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='post')
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='tags')
    nation = models.OneToOneField('Nationality', on_delete=models.CASCADE, null=True, related_name='nation')
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
    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

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


class Nationality(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    birth_place = models.TextField()
    child = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Национальность: {self.name}. Место рождения: {self.birth_place}"