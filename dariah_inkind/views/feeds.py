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

from django.core.urlresolvers import reverse_lazy
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext_lazy as _

from ..models import Contribution


class ContributionsFeed(Feed):
    title = _("Contributions Feed")
    link = reverse_lazy('dariah_inkind:feed')
    description = _("Updates on changes and additions to DARIAH contributions.")
    author_name = _("DARIAH")
    author_link = _("http://dariah.eu")

    def items(self):
        return Contribution.objects.published()

    def item_title(self, item):
        return item.dc_title

    def item_description(self, item):
        return item.dc_description

    def item_pubdate(self, item):
        return item.last_modified_on

    def item_author_name(self, item):
        return item.dc_publisher


class ContributionsAtomFeed(ContributionsFeed):
    feed_type = Atom1Feed
    subtitle = ContributionsFeed.description
    link = reverse_lazy('dariah_inkind:feed_atom')
