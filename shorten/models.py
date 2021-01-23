from shorten.utils import code_generator
from django.db import models
from django.contrib.auth.models import User
from .utils import create_shortcode
from bs4 import BeautifulSoup
import requests
# Create your models here.


class ShortURL(models.Model):
    """
        docstring
    """
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=15, unique=True,  blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    url_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        self.url_name = self.get_url_name()
        return super(ShortURL, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "localhost:8000/" + self.shortcode

    def get_url_name(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.title.text if soup.title else str(self.url)
