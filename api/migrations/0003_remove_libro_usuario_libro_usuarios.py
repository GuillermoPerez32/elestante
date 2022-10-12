# Generated by Django 4.1.1 on 2022-10-12 02:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_material_remove_modulo_cantidad_unidades_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='usuario',
        ),
        migrations.AddField(
            model_name='libro',
            name='usuarios',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='usuarios'),
        ),
    ]
