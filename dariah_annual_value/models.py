from django.db import models

import datetime

from django.core.urlresolvers import reverse

#from django.utils.translation import ugettext_lazy as _
    
YEAR_CHOICES = []
for y in range(2000, 2026):
    YEAR_CHOICES.append((y,y))

# Create your models here.
class AnnualValue(models.Model):
        inkind = models.ForeignKey("dariah_inkind.Contribution",  null=False, blank=False)
        value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="In euro")
        justification = models.CharField(max_length=1000, null=True, blank=True, help_text="Help text for 'justification'")
        year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year,  help_text="Help text for 'Year'")
        
        #@property
        #def value(self):
        #    return "\u20AC%s" % self.value
        
        
        def get_absolute_url(self):
            return reverse('dariah_annual_value:detail', kwargs={'pk': self.pk})
        
        
        # Other ###################################################################
        field_order = [  # (name, in form?, meta-metadata field?)
            ('value', 1, 0),
            ('justification', 1, 0),
            ('year', 1, 0),
        ]