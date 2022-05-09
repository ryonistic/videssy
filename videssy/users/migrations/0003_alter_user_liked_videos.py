# Generated by Django 4.0.4 on 2022-05-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0004_video_dislikes_video_likes_comment'),
        ('users', '0002_user_liked_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='liked_videos',
            field=models.ManyToManyField(blank=True, to='vlog.video'),
        ),
    ]