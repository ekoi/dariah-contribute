from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Contribution(models.Model):
    title = models.CharField(max_length=100)
    relation = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    coverage = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    abstract = models.CharField(max_length=2000, blank=True)
    description = models.CharField(max_length=5000, blank=True)
    contributor = models.CharField(max_length=50, blank=True)
    vocabulary = models.CharField(max_length=50, blank=True)
    creator=models.OneToOneField(User, verbose_name="Creator")
    date = models.DateTimeField(default="2014-01-01")
    publish_date = models.DateTimeField('date published', default=datetime.now)
    modify_date = models.DateTimeField('date modified', default=datetime.now)

    def __unicode__(self):
        return self.title

        fields = ['title', 'date', 'relation', 'publisher', 'coverage', 'subject', 'abstract', 'description', 'contributor', 'vocabulary', ]
