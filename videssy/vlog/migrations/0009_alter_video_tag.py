# Generated by Django 4.0.4 on 2022-05-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0008_alter_video_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tag',
            field=models.CharField(choices=[('asmr', 'asmr'), ('gaming', 'gaming'), ('vlog', 'vlog'), ('music', 'music'), ('animation', 'animation')], max_length=100, null=True),
        ),
    ]