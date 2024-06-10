from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    
    subheading1 = models.CharField(max_length=100)
    subheading2 = models.CharField(max_length=100)
    subheading3 = models.CharField(max_length=100)
    subheading4 = models.CharField(max_length=100)
    subheading5 = models.CharField(max_length=100)
    subheading6 = models.CharField(max_length=100)
    subheading7 = models.CharField(max_length=100)
    subheading7 = models.CharField(max_length=100)

    content1 = models.TextField(max_length=1000)
    content2 = models.TextField(max_length=1000)
    content3 = models.TextField(max_length=1000)
    content4 = models.TextField(max_length=1000)
    content5 = models.TextField(max_length=1000)
    content6 = models.TextField(max_length=1000)
    content7 = models.TextField(max_length=1000)
    content8 = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog_images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
