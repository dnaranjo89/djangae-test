from google.appengine.ext import db


class Category(db.Model):
    name = db.StringProperty()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Article(db.Model):
    title = db.StringProperty()
    views = db.IntegerProperty()
    category = db.ReferenceProperty(Category)
    '''category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    image = models.URLField()
    tags = models.CharField(max_length=100)
    views = models.IntegerField(default=0)'''

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title