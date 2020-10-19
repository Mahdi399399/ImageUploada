from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
  # '''users/%Y/%m/%d/'''
'''def get_absolute_url(self):  # new

    return reverse('post_detail', args=[str(self.id)])'''