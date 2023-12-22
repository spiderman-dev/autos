# Generated by Django 5.0 on 2023-12-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('titulo', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('propietario', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=14)),
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
    ]