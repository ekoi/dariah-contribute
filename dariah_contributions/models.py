from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Contribution(models.Model):
    title = models.CharField(max_length=100)
    contributor = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    creator=models.OneToOneField(User, verbose_name="Creator")
    publish_date = models.DateTimeField('date published', default=datetime.now)
    modify_date = models.DateTimeField('date modified', default=datetime.now)

    def __unicode__(self):
        return self.title
