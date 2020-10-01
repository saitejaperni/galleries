from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Actress(models.Model):
    name= models.CharField(max_length=50)
    bannerImage = models.ImageField(upload_to='media/', null=True)
    slug=models.SlugField()
    def __str__(self):
        return f"{self.name}"
    def get_absolute_url(self):
        return reverse("actressalbums", kwargs={"id":self.id, "slug": self.slug })
class Albums(models.Model):
    title = models.CharField(max_length=100)
    body=RichTextField(blank=True, null=True)
    bannerImage= models.ImageField(upload_to = 'media/', null= True)
    actress=models.ForeignKey(Actress, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("albumsdetail", kwargs={"id":self.id})


class carouselslide(models.Model):
       title= models.CharField(max_length=50)
       image1=models.ImageField(upload_to='media/')

       def __str__(self):
           return self.title

class carouselslideX(models.Model):
    title=models.CharField(max_length=50)
    image2 = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title