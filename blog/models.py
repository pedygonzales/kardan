from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    post_title = models.CharField(max_length=250)
    body = models.TextField(max_length=300, null=True)
    post_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_list', kwargs={'pk': self.pk})
