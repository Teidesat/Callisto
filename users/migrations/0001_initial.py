# Generated by Django 5.2.1 on 2025-05-12 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('V', 'Voluntario'), ('S', 'Estudiante')], default='S', max_length=1)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(blank=True, default='cache/noavatar.png', null=True, upload_to='cache')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
