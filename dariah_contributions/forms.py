import autocomplete_light
from django.forms import CheckboxSelectMultiple
from autocomplete_light.contrib.taggit_field import TaggitWidget
autocomplete_light.autodiscover()

from .models import Contribution


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
        widgets = {'dc_subject': TaggitWidget('TagAutocomplete'),
                   'skos_preflabel_vcc': CheckboxSelectMultiple}
        autocomplete_names = {'skos_preflabel_technique': 'TADIRAHTechniqueAutocomplete',
                              'skos_preflabel_activity': 'TADIRAHActivityAutocomplete',
                              'skos_preflabel_object': 'TADIRAHObjectAutocomplete',
                              'skos_preflabel_discipline': 'DisciplineAutocomplete',
                              'dc_contributor': 'DcContributorAutocomplete',
                              'dc_creator': 'DcCreatorAutocomplete'}
