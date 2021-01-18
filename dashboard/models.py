from django.db import models
from shorten.models import ShortURL
# Create your models here.


class Click(models.Model):
    click_date = models.DateField(auto_now=True, auto_now_add=False)
    country = models.CharField(max_length=2, blank=True, null=True)
    os = models.CharField(max_length=7, blank=True, null=True)
    referer = models.CharField(max_length=200, blank=True, null=True)
    shorturl = models.ForeignKey(ShortURL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shorturl.url)
