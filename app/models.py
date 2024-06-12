from django.db import models

# Create your models here.


class Post(models.Model):
    photo = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title