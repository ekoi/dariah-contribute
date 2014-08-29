import autocomplete_light
from autocomplete_light.contrib.taggit_field import TaggitWidget
autocomplete_light.autodiscover()

from .models import Contribution


class ContributionForm(autocomplete_light.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Contribution
        fields = [
            'skos_preflabel_technique',
            #'dc_identifier',
            'dc_title',
            'dc_date',
            'dc_relation',
            'vcard_logo',
            'dc_publisher',
            'dc_coverage',
            'vcard_organization',
            'dc_subject',
            'dcterms_abstract_en',
            'dcterms_abstract',
            'dcterms_abstract_lang',
            'dc_description',
            'dc_creator',
            'dc_contributor',
            #'author',
            'is_published',
            'published_on',
            #'last_modified_on',
            #'is_deleted'
        ]
        widgets = {'dc_subject': TaggitWidget('TagAutocomplete'), }
        autocomplete_names = {'skos_preflabel_technique': 'TADIRAHTechniqueAutocomplete', }
