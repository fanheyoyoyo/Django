from django.db import models
from datetime import date


# Create your models here.
class BookInfo(models.Model):
    bTitle = models.CharField(max_length=30)
    bType = models.CharField(max_length=30, blank=True)
    bAuthor = models.CharField(max_length=30, blank=True)
    bComment = models.TextField(max_length=200, blank=True)
    bPubDate = models.DateField(default=date.today, blank=True)
    bHaveRead = models.BooleanField(default=False, blank=True)
    bTxt = models.FileField(upload_to='./Txt/', max_length=200, blank=True)
    bUrl = models.URLField(blank=True)
    bCover = models.ImageField(upload_to='./Image/', height_field=100, width_field=150, max_length=200, blank=True)

    def __unicode__(self):
        return self.bTitle


class HeroInfo(models.Model):
    hName = models.CharField(max_length=30)
    hGender = models.CharField(max_length=1, blank=True)
    hContent = models.TextField(max_length=200, default='', blank=True)
    hBook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.hName


class God(models.Model):
    gName = models.CharField(max_length=30)
    gAge = models.IntegerField(blank=True)
    gEmail = models.EmailField(default='', unique=True)
    gLastReadDate = models.DateField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.gName