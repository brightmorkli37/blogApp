# Generated by Django 3.1.11 on 2021-06-11 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]