from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo")
    token = models.CharField(max_length=64)


class FreeCourse(models.Model):
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=32)
    price = models.CharField(max_length=32)


class SeniorCourse(models.Model):
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=32)
    price = models.CharField(max_length=32)