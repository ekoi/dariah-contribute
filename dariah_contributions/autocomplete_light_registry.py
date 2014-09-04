from django.core.urlresolvers import reverse

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
        return '<span class="block"><em>%s</em></span> \
        <hr class="divider" /> \
        <span class="block"><em><a data-toggle="modal" data-target="#myModal" id="add_id_dc_creator" class="autocomplete-add-another" href="' + reverse(self.add_another_url_name) + '?_popup=1">Add new...</a></em></span>'


class DcContributorAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^first_name', 'last_name_prefix', 'last_name']
    model = DcContributor
    add_another_url_name = 'dariah_contributions:dccontributor_create'

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
        return '<span class="block"><em>%s</em></span> \
        <hr class="divider" /> \
        <span class="block"><em><a data-toggle="modal" data-target="#myModal" id="add_id_dc_contributor" class="autocomplete-add-another" href="' + reverse(self.add_another_url_name) + '?_popup=1">Add new...</a></em></span>'


autocomplete_light.register(Tag)
autocomplete_light.register(DcCreator, DcCreatorAutocomplete)
autocomplete_light.register(DcContributor, DcContributorAutocomplete)
