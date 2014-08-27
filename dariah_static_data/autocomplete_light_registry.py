import autocomplete_light
from .models import TADIRAHTechnique


autocomplete_light.register(TADIRAHTechnique,
    search_fields=['^name', ],  # Just like in ModelAdmin.search_fields
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Technique item...?',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    }
)
