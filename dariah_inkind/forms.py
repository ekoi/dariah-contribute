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

import autocomplete_light
from django.db.models.base import Model
# from dariah_inkind.models import DcPerson
autocomplete_light.autodiscover()

from .models import Contribution
from .models import DcContributor
from .models import DcCreator


class ContributionForm(autocomplete_light.ModelForm):
    required_css_class = 'required'

    readonly_fields = [  # Not a django ModelForm attribute
        'dc_identifier',
        'author',
        'published_on',
        'last_modified_on',
        #'is_deleted'
    ]

    class Meta:
        model = Contribution
        fields = [x[0] for x in Contribution.field_order if x[1]]
        autocomplete_names = {'skos_preflabel_technique': 'TADIRAHTechniqueAutocomplete',
                              'skos_preflabel_activity': 'TADIRAHActivityAutocomplete',
                              'skos_preflabel_object': 'TADIRAHObjectAutocomplete',
                              'skos_preflabel_discipline': 'DisciplineAutocomplete',
                              'dc_contributor': 'DcContributorAutocomplete',
                              'dc_creator': 'DcCreatorAutocomplete'}
        
class DcCreatorForm(autocomplete_light.ModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = DcCreator
        
class DcContributorForm(autocomplete_light.ModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = DcContributor
        
# class DcPersonForm(autocomplete_light.ModelForm):
#     required_css_class = 'required'
#     
#     class Meta:
#         model = DcPerson
#     
    
