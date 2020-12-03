from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class new1(models.Model):
    """docstring for new1."""

    head = models.CharField(max_length=100, default=None)
    conte = models.TextField(max_length=200, default=None)
    price = models.IntegerField
    image  = models.ImageField(upload_to="static/img" ,default=None)
