# Generated by Django 5.1.6 on 2025-02-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, help_text='The arcane category of the blog', max_length=100, null=True),
        ),
    ]
