from django.db import models
from django.utils.text import slugify
from django.conf import settings
from PIL import Image

from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Video(models.Model):
    TAG_CHOICES = (
            ('1','asmr'),
            ('2','gaming'),
            ('3','vlog'),
            ('4','music'),
            ('5','animation'),
            )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    footage = models.FileField(upload_to='videos/')
    likes = models.PositiveBigIntegerField(default=0)
    tag = models.CharField(choices=TAG_CHOICES,max_length=100, null=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        thumbnail = Image.open(self.thumbnail.path)
        if thumbnail.height > 700 or thumbnail.width > 700:
            output_size = (700, 700)
            thumbnail.thumbnail(output_size)
            thumbnail.save(self.thumbnail.path)
    class Meta:
        ordering = ['-published']

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    published = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)
