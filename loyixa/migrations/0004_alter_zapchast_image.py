# Generated by Django 4.2.11 on 2024-04-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyixa', '0003_alter_zapchast_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapchast',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
