# Generated by Django 5.1.6 on 2025-02-19 12:42

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The enchanted name of the project', max_length=200)),
                ('description', models.TextField(help_text="A mystical scroll detailing the project's purpose")),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('technologies', models.CharField(help_text='Magical spells (tech stack) used', max_length=300)),
                ('live_demo', models.URLField(blank=True, help_text='Portal to the live project', null=True)),
                ('source_code', models.URLField(blank=True, help_text='Ancient scroll of source code', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_projects', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wizard_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Etch your arcane wisdom here (comment)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_spellcasters', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_comments', to='projects.project')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
