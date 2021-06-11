from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')  # , kwargs={'pk': self.name}

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-name', )

class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=105)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    # body = models.TextField()
    body = RichTextField()
    date_published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, max_length=50)

    def summary(self):
        return self.body[:65]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        ordering = ('-date_published',)