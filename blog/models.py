from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    CATEGORY_CHOICES = (
        ('software', 'software'),
        ('technology', 'technology'),
        ('news', 'news')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=105)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()
    date_published = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:120]

    class Meta:
        ordering = ('-date_published',)