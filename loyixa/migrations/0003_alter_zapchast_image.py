# Generated by Django 4.2.11 on 2024-04-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyixa', '0002_maxsulot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapchast',
            name='image',
            field=models.ImageField(upload_to='media-files'),
        ),
    ]
