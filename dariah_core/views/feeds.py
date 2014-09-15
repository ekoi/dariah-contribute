from django.core.urlresolvers import reverse_lazy
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext_lazy as _

from ..models import Contribution


class ContributionsFeed(Feed):
    title = _("Contributions Feed")
    link = reverse_lazy('dariah_core:feed')
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
    link = reverse_lazy('dariah_core:feed_atom')
