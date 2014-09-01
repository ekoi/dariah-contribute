import autocomplete_light
from autocomplete_light.contrib.taggit_field import TaggitWidget
autocomplete_light.autodiscover()

from .models import Contribution


class ContributionForm(autocomplete_light.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Contribution
        fields = [x[0] for x in Contribution.field_order if x[1]]
        widgets = {'dc_subject': TaggitWidget('TagAutocomplete'), }
        autocomplete_names = {'skos_preflabel_technique': 'TADIRAHTechniqueAutocomplete', }
