# Generated by Django 5.0 on 2023-12-20 18:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_fiado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiado',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]