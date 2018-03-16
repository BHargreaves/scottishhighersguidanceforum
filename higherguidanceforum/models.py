from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name

class Link(models.Model):

    category = models.ForeignKey(Subject)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    #Links UserProfile to a user model instance
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Teachers(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.user.teachername


