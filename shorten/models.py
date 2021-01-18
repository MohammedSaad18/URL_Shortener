from shorten.utils import code_generator
from django.db import models
from django.contrib.auth.models import User
from .utils import create_shortcode
# Create your models here.
class ShortURL(models.Model):
    """
        docstring
    """
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=15,unique=True,  blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        return super(ShortURL,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "localhost:8000/"+ self.shortcode


