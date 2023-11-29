from django.db import models
from accounts.models import UserProfile

# Create your models here.
STATUS = (
    ('OPEN', 'OPEN'),
    ('CLOSE', 'CLOSE'),
)


class Pharmacy(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    country = models.CharField(max_length=120)
    town = models.CharField(max_length=120)
    quarter = models.CharField(max_length=120)
    localisation = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='doc')
    image = models.ImageField(upload_to='doc')
    status = models.CharField(max_length=25, choices=STATUS, default='OPEN')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Advice(models.Model):
    author = models.CharField(max_length=120, default='Unknown')
    content = models.TextField(max_length=500)
