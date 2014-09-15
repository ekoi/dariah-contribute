from django.template.loader import render_to_string

from taggit.models import Tag
from .models import DcCreator, DcContributor

import autocomplete_light


class DcCreatorAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^first_name', 'last_name_prefix', 'last_name']
    model = DcCreator
    add_another_url_name = 'dariah_contributions:dccreator_create'

    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs = {}

    @property
    def empty_html_format(self):
        data = {'model': self.model.lowercase_underscore_name(),
                'url': self.add_another_url_name}
        return render_to_string('dariah_contributions/_creator-contrib_autocomplete_empty_html_format.html', data)


class DcContributorAutocomplete(DcCreatorAutocomplete):
    model = DcContributor
    add_another_url_name = 'dariah_contributions:dccontributor_create'


autocomplete_light.register(Tag)
autocomplete_light.register(DcCreator, DcCreatorAutocomplete)
autocomplete_light.register(DcContributor, DcContributorAutocomplete)
