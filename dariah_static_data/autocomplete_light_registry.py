import autocomplete_light
from .models import TADIRAHTechnique, TADIRAHActivity, TADIRAHObject, Discipline


class TADIRAHTechniqueAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = TADIRAHTechnique
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class TADIRAHActivityAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^activity_group_name', '^activity_name']
    model = TADIRAHActivity
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class TADIRAHObjectAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = TADIRAHObject
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs = {
        #'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        #'class': 'modern-style',
    }


class DisciplineAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = Discipline
    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
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
