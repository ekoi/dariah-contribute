from django.db import models

import datetime

from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
#from django.utils.translation import ugettext_lazy as _
from dariah_inkind.models import Contribution
from django.contrib.auth import get_user_model
User = get_user_model()


# Managers
class AnnualValueMixin(object):
#     def by_author(self, user):
#         kwargs = {'is_deleted': False,
#                   'author': user}
#         return self.filter(**kwargs)
    
    def by_author(self, user):
        mycontributes = Contribution.objects.by_author(user)
        print '------', mycontributes 
        kwargs = {'inkind': mycontributes}
        return self.filter(**kwargs)


class AnnualValueQuerySet(QuerySet, AnnualValueMixin):
    pass


class AnnualValueManager(models.Manager, AnnualValueMixin):
    
    def get_query_set(self):
        return AnnualValueQuerySet(self.model, using=self._db)   
    
YEAR_CHOICES = []
for y in range(2014, 2026):
    YEAR_CHOICES.append((y,y))
    



# Create your models here.
class AnnualValue(models.Model):
        
        inkind = models.ForeignKey("dariah_inkind.Contribution",  null=False, blank=False, help_text="Inkind help text")
        materialcost = models.IntegerField(null=True, blank=True, verbose_name="Total Material Cost", help_text="In euro")
        personnelcost = models.IntegerField(null=True, blank=True, verbose_name="Total Personnel Cost", help_text="In euro")
        justification = models.CharField(max_length=1000, null=True, blank=True, help_text="Help text for 'justification'")
        year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year,  help_text="Help text for 'Year'")
        
        #@property
        #def value(self):
        #    return "\u20AC%s" % self.value
        class Meta:
            verbose_name = 'annualvalue'
        
        
        @staticmethod
        def int_format(value, decimal_points=3, seperator=u'.'):
            newValue = str(value)
            if len(newValue) <= decimal_points:
                return newValue
            # say here we have value = '12345' and the default params above
            parts = []
            while newValue:
                parts.append(newValue[-decimal_points:])
                newValue = newValue[:-decimal_points]
            # now we should have parts = ['345', '12']
            parts.reverse()
            # and the return value should be u'12.345'
            return seperator.join(parts)
        
        def get_absolute_url(self):
            return reverse('dariah_annual_value:detail', kwargs={'pk': self.pk})
        
        def get_materialcost_format(self):
            value = self.int_format(self.materialcost)
            return value
        
        def get_personnelcost_format(self):
            value = self.int_format(self.personnelcost)
            return value
            
        
        # Managers ################################################################
        objects = AnnualValueManager()
        
        # Other ###################################################################
        field_order = [  # (name, in form?, meta-metadata field?)
            ('materialcost', 1, 0),
            ('personnelcost', 1, 0),
            ('justification', 1, 0),
            ('year', 1, 0),
        ]
        
        
