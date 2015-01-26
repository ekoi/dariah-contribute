from django.db import models

import datetime

    
YEAR_CHOICES = []
for y in range(2000, 2026):
    YEAR_CHOICES.append((y,y))

# Create your models here.
class AnnualValue(models.Model):
        inkind = models.ForeignKey("dariah_inkind.Contribution",  null=False, blank=False)
        value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="In euro")
        justification = models.CharField(max_length=500, null=True, blank=True, help_text="Write down the justification of the project.")
        year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        
        #@property
        #def value(self):
        #    return "\u20AC%s" % self.value
        
        