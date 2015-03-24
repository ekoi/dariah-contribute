"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.

    Copyright 2014 Data Archiving and Networked Services

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from django.utils.translation import ugettext as _
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin

from ..models import DcCreator

class DcPersonDetailMixin(BaseDetailView):
    model = DcCreator

    def get_context_data(self, **kwargs):
        context = super(DcPersonDetailMixin, self).get_context_data(**kwargs)
        c = context['object']
        context['get_fields'] = self.get_fields(c)
        context['get_metadata_fields'] = self.get_fields(c, True)
        return context

    def get_fields(self, c, meta_metadata=False):
        """An iterable with the field names and values (in the correct order)
        of a DcPerson instance to be rendered in the template.
        """
       
        fields = c.field_order
        for x in fields:
            field = c.__class__._meta.get_field(x[0])
            value = getattr(c, x[0])
            is_safe = False
            help_text = unicode(field.help_text)
            # If the field is an iterable (TaggableManager or ManyToManyField)
            # format the data as a string of comma separated items.
            yield field.verbose_name, value, is_safe, help_text

   



class DcPersonDetail(DcPersonDetailMixin, SingleObjectTemplateResponseMixin):
    pass


