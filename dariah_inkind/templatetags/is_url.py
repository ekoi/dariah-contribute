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

from django import template
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils import safestring
from dariah_inkind.models import DcContributor


register = template.Library()


@register.filter
def is_url(value):
    """Checks if the given value is a URL."""
    v = URLValidator()
    try:
        v(value)
    except ValidationError:
        return False
    return True

@register.simple_tag
def add_active(name):
    """ Return the string 'active' current request.path is same as name
    Keyword aruguments:
    request -- Django request object
    name -- name of the url or the actual path
    by_path -- True if name contains a url instead of url name
    """
    print '==================================\n', name
    return 'EKO' + name

@register.filter
def autocomplete_light_choice_html2(choice, autocomplete):
    """Return autocomplete.choice_html(choice)"""
    value = autocomplete.choice_html(choice)
    new_foaf_name = ''
    if type(choice) is DcContributor:
        new_foaf_name='<a href="/inkind/dc_contributor/' + str(choice.id) + '">' + choice.foaf_name + '</a>'
    else:
        new_foaf_name='<a href="/inkind/dc_creator/' + str(choice.id) + '">' + choice.foaf_name + '</a>'
    
    newValue = value.replace(choice.foaf_name, new_foaf_name)
    return safestring.mark_safe(newValue)
