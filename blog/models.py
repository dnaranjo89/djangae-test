from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    image = models.URLField()
    tags = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title