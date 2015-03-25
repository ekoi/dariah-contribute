from django.db import models

import datetime

from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


# Managers
class PersonMixin(object):
#     def by_author(self, user):
#         kwargs = {'is_deleted': False,
#                   'author': user}
#         return self.filter(**kwargs)
    
    def by_author(self, user):
        return self.all


class PersonQuerySet(QuerySet, PersonMixin):
    pass


class PersonManager(models.Manager, PersonMixin):
    
    def get_query_set(self):
        return PersonQuerySet(self.model, using=self._db)   
    



# Create your models here.
class Person(models.Model):
    first_name = models.CharField(
        max_length=50,
        help_text=_('help text for first name'))
    last_name_prefix = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('help text for last name prefix'))
    last_name = models.CharField(
        max_length=50,
        help_text=_('help text for last name'))
    foaf_email = models.EmailField(
        verbose_name=_("Email address"),
        help_text=_('help text for email address'))
    foaf_person = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('help text for foaf:person'))

    @property
    def uri(self):
        return self.foaf_person

    @property
    def foaf_name(self):
        if self.last_name_prefix:
            name = u"%s %s %s (%s)" % (self.first_name,
                                 self.last_name_prefix,
                                 self.last_name, self.foaf_email)
        else:
            name = u"%s %s (%s)" % (self.first_name,
                              self.last_name, self.foaf_email)
        return name

    def get_absolute_url(self):
        return reverse('dariah_person:detail', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return self.foaf_name


    @classmethod
    def lowercase_underscore_name(cls):
        """Transform class name from CamelCase to lowercase_with_underscores."""
        return re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', cls.__name__).lower().strip('_')


    
    field_order = [('first_name', 1, 0),('last_name_prefix', 1, 0), ('last_name', 1, 0), ('foaf_email', 1, 0), ('foaf_person', 1, 0)]
    
    class Meta:
        verbose_name = 'person'
        
        
      
        
