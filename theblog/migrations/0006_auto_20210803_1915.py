# Generated by Django 3.2.5 on 2021-08-03 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]