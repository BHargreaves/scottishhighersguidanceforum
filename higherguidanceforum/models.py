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


class Question(models.Model):

    category = models.ForeignKey(Subject)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title


class Answer(models.Model):

    category = models.ForeignKey(Question)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1999)

    class Meta:
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.title



class UserProfile(models.Model):
    #Links UserProfile to a user model instance
    user = models.OneToOneField(User)
    usubjects = models.ManyToManyField(Subject, related_name='usubjects')

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


#How to create the different types of users is referenced from the following site:
#https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html

class Student(models.Model):

    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    teacher = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Admin(models.Model):

    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
