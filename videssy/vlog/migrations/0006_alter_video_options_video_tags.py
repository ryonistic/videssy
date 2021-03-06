# Generated by Django 4.0.4 on 2022-05-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0005_remove_video_dislikes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-published']},
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.CharField(blank=True, choices=[('1', 'asmr'), ('2', 'gaming'), ('3', 'vlog'), ('4', 'music'), ('5', 'animation')], max_length=100, null=True),
        ),
    ]
