# Generated by Django 3.1.4 on 2021-02-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default='test', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]