# Generated by Django 3.1.4 on 2021-02-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0002_auto_20210206_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
