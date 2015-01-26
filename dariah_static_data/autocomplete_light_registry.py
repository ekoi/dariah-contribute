"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contribss.

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
from .models import TADIRAHTechnique, TADIRAHActivity, TADIRAHObject, Discipline


class TADIRAHTechniqueAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = TADIRAHTechnique
    limit_choices = 1000
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 0,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class TADIRAHActivityAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^activity_group_name', '^activity_name']
    model = TADIRAHActivity
    limit_choices = 1000
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 0,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class TADIRAHObjectAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = TADIRAHObject
    limit_choices = 1000
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 0,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class DisciplineAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = Discipline
    limit_choices = 1000
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 0,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


"""Note: adding the model as the first argument is a temporary fix for
https://github.com/yourlabs/django-autocomplete-light/issues/313.
"""
autocomplete_light.register(TADIRAHTechnique, TADIRAHTechniqueAutocomplete)
autocomplete_light.register(TADIRAHActivity, TADIRAHActivityAutocomplete)
autocomplete_light.register(TADIRAHObject, TADIRAHObjectAutocomplete)
autocomplete_light.register(Discipline, DisciplineAutocomplete)
