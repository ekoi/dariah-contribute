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

from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse
from pycountry import languages as l
from taggit.managers import TaggableManager
import os.path
import re
import uuid

from django.contrib.auth import get_user_model
User = get_user_model()

from .storage import OverwriteStorage


# Managers
class ContributionMixin(object):
    def by_author(self, user):
        kwargs = {'is_deleted': False,
                  'author': user}
        return self.filter(**kwargs)

    def published(self):
        kwargs = {'is_deleted': False,
                  'is_published': True,
                  'published_on__lte': timezone.now()}
        return self.filter(**kwargs)

    def published_or_by_author(self, user):
        if user.is_authenticated():
            return self.filter(Q(is_deleted=False) &                     # Not deleted and
                               ((Q(is_published=True) &
                                 Q(published_on__lte=timezone.now())) |  # Either Published
                                Q(author=user)))                         # or by current user
        return self.published()


class ContributionQuerySet(QuerySet, ContributionMixin):
    pass


class ContributionManager(models.Manager, ContributionMixin):
    def get_query_set(self):
        return ContributionQuerySet(self.model, using=self._db)


class PublishedContributionsManager(models.Manager):
    """Filters out all unpublished items and items with a publication date in the future."""
    def get_queryset(self):
        kwargs = {'is_deleted': False,
                  'is_published': True,
                  'published_on__lte': timezone.now()}
        return super(PublishedContributionsManager, self).get_query_set().filter(**kwargs)


def contribution_vcardlogo_uploadto(instance, filename):
    """Redefine the image path/name.
    Based on:
    http://www.malloc.co/django/django-rename-a-file-uploaded-by-a-user-before-saving/
    """
    # get extension from raw filename
    fn, ext = os.path.splitext(filename)
    new_filename = uuid.uuid4().hex
    path = 'contribution_vcardlogo'
    # return new filename, including its parent directories (based on MEDIA_ROOT)
    return "{path}/{new_filename}{ext}".format(path=path,
                                               new_filename=new_filename,
                                               ext=ext)


class Contribution(models.Model):
    # CHOICES Definitions #####################################################
    DCTERMS_ABSTRACT_LANG_CHOICES = filter(lambda x: x[0] and x[1],
                                           map(lambda x: (getattr(x, 'alpha2', None),
                                                          getattr(x, 'name', None)),
                                               l))
    DC_DATE_CHOICES = [(x, x) for x in reversed(xrange(1900, timezone.now().year + 1))]
    # Metadata fields #########################################################
    # dc_type = models.URLField(
    #     _("dc:type"),
    #     blank=True,
    #     null=True,
    #     help_text=_('help text for dc:type'))
    # vcard_category = models.URLField(
    #     _("vcard:category"),
    #     blank=True,
    #     null=True,
    #     help_text=_('help text for vcard:category'))
    dc_identifier = models.AutoField(
        _("dc:identifier"),
        primary_key=True,
        help_text=_('help text for dc:identifier'))
    dc_title = models.CharField(
        _("dc:title"),
        max_length=100,
        help_text=_('help text for dc:title'))
    dc_date = models.PositiveIntegerField(
        _("dc:date"),
        choices=DC_DATE_CHOICES,
        max_length=4,  # YYYY IS ISO-8601, see https://en.wikipedia.org/wiki/ISO_8601#Years
        blank=True,
        help_text=_('help text for dc:date'))
    dc_relation = models.URLField(
        _("dc:relation"),
        max_length=200,
        blank=True,
        help_text=_("help text for dc:relation"))
    vcard_logo = models.ImageField(
        _("vcard:logo"),
        upload_to=contribution_vcardlogo_uploadto,
        storage=OverwriteStorage(),
        blank=True,
        null=True,
        help_text=_('help text for vcard:logo'))
    dc_publisher = models.CharField(
        _("dc:publisher"),
        max_length=200,
        blank=True,
        help_text=_("help text for dc:publisher"))
    dcterms_spatial = models.CharField(
        _("dcterms:spatial"),
        blank=True,
        max_length=255,
        help_text=_('help text for dcterms:spatial'))
    dc_coverage = models.ForeignKey(
        'dariah_static_data.Country',
        verbose_name=_("dc:coverage"),
        blank=True,
        null=True,
        help_text=_('help text for dc:coverage'))
    vcard_organization = models.CharField(
        _("vcard:organization"),
        max_length=50,
        blank=True,
        help_text=_("help text for vcard:organization"))
    dc_subject = TaggableManager(
        verbose_name=_("dc:subject"),
        blank=True,
        help_text=_('help text for dc:subject'))
    dcterms_abstract_en = models.TextField(
        _("dcterms:abstract English"),
        help_text=_('help text for dcterms:abstract English'))
    dcterms_abstract = models.TextField(
        _("dcterms:abstract alternative language"),
        blank=True,
        help_text=_('help text for dcterms:abstract alternative language'))
    dcterms_abstract_lang = models.CharField(
        _("dcterms:abstract language"),
        max_length=2,
        choices=DCTERMS_ABSTRACT_LANG_CHOICES,
        default='en',
        blank=True,
        help_text=_('help text for dcterms:abstract language'))
    dc_description = models.TextField(
        _("dc:description"),
        blank=True,
        help_text=_('help text for dc:description'))
    skos_preflabel_activity = models.ManyToManyField(
        'dariah_static_data.TADIRAHActivity',
        verbose_name=_('sioc:topic/skos:Concept/skos:prefLabel Activity'),
        blank=True,
        null=True,
        help_text=_('help text for skos:preflabel Activity')
    )
    skos_preflabel_object = models.ManyToManyField(
        'dariah_static_data.TADIRAHObject',
        verbose_name=_('sioc:topic/skos:Concept/skos:prefLabel Object'),
        blank=True,
        null=True,
        help_text=_('help text for skos:preflabel Object')
    )
    skos_preflabel_technique = models.ManyToManyField(
        'dariah_static_data.TADIRAHTechnique',
        verbose_name=_('sioc:topic/skos:Concept/skos:prefLabel Technique'),
        blank=True,
        null=True,
        help_text=_('help text for skos:preflabel Technique')
    )
    skos_preflabel_discipline = models.ManyToManyField(
        'dariah_static_data.Discipline',
        verbose_name=_('sioc:topic/skos:Concept/skos:prefLabel Discipline'),
        blank=True,
        null=True,
        help_text=_('help text for skos:preflabel Discipline')
    )
    skos_preflabel_vcc = models.ManyToManyField(
        'dariah_static_data.TADIRAHVCC',
        verbose_name=_('sioc:has_scope/skos:Concept/skos:prefLabel VCC'),
        blank=True,
        null=True,
        help_text=_('help text for skos:preflabel VCC')
    )
    dc_creator = models.ManyToManyField(
        'DcCreator',
        verbose_name=_("dc:creator"),
        blank=True,
        null=True,
        help_text=_('help text for dc:creator'))
    dc_contributor = models.ManyToManyField(
        'DcContributor',
        verbose_name=_("dc:contributor"),
        blank=True,
        null=True,
        help_text=_('help text for dc:contributor'))

    # Meta-Metadata fields ####################################################
    author = models.ForeignKey(
        User,
        verbose_name=_('author'),
        editable=False,
        blank=True,
        null=True,
        help_text=_('help text for author'))
    is_published = models.BooleanField(
        _('is published?'),
        default=False,
        help_text=_('help text for is_published'))
    published_on = models.DateTimeField(
        _('published on'),
        blank=True,
        null=True,
        editable=False,
        help_text=_('help text for published_on'))
    last_modified_on = models.DateTimeField(
        _('last modified on'),
        default=timezone.now,
        editable=False,
        help_text=_('help text for last_modified'))
    is_deleted = models.BooleanField(
        _('is deleted?'),
        default=False,
        editable=False,
        help_text=_('help text for is_deleted'))

    # Managers ################################################################
    objects = ContributionManager()
    published = PublishedContributionsManager()

    # Other ###################################################################
    field_order = [  # (name, in form?, meta-metadata field?)
        #('dc_type', 1, 0),
        #('vcard_category', 1, 0),
        ('dc_identifier', 0, 0),
        ('dc_title', 1, 0),
        ('dc_date', 1, 0),
        ('dc_relation', 1, 0),
        ('vcard_logo', 1, 0),
        ('dc_publisher', 1, 0),
        ('vcard_organization', 1, 0),
        ('dcterms_spatial', 1, 0),
        ('dc_coverage', 1, 0),
        ('dc_subject', 1, 0),
        ('dcterms_abstract_en', 1, 0),
        ('dcterms_abstract', 1, 0),
        ('dcterms_abstract_lang', 1, 0),
        ('dc_description', 1, 0),
        ('skos_preflabel_activity', 1, 0),
        ('skos_preflabel_object', 1, 0),
        ('skos_preflabel_technique', 1, 0),
        ('skos_preflabel_discipline', 1, 0),
        ('skos_preflabel_vcc', 1, 0),
        ('dc_creator', 1, 0),
        ('dc_contributor', 1, 0),
        ('author', 0, 1),
        ('is_published', 1, 1),
        ('published_on', 0, 1),
        ('last_modified_on', 0, 1),
        #('is_deleted', 0, 1)
    ]

    def __unicode__(self):
        return self.dc_title

    def get_absolute_url(self):
        return reverse('dariah_inkind:detail', kwargs={'pk': self.pk})

    def attrs(self):
        patt = re.compile('_id$')
        for attr, value in self.__dict__.iteritems():
            if not attr.startswith('_'):  # Extract private attributes
                yield self._meta.get_field(patt.sub('', attr)).verbose_name, value

    def has_owner(self, user):
        return self.author == user

    class Meta:
        ordering = ['-published_on', ]
        get_latest_by = 'published_on'
        verbose_name = _('contribution')
        verbose_name_plural = _('contributions')

    def save(self, *args, **kwargs):
        """Add published_on date is now if published is True.
        Or if the publication is republished, also set the published_on
        date to now.
        """
        if self.is_published and not self.published_on:
            self.published_on = timezone.now()
        else:
            try:
                # Get the old object currently in the database
                old_object = Contribution.objects.get(pk=self.pk)
            except Contribution.DoesNotExist:
                pass
            else:
                # If the object was republished, change the datetime
                if not old_object.is_published and self.is_published:
                    self.published_on = timezone.now()
        """ Always add last_modified_on date """
        self.last_modified_on = timezone.now()
        super(Contribution, self).save(*args, **kwargs)


class Person(models.Model):
    foaf_person = models.URLField(
        blank=True,
        help_text=_('help text for foaf:person'))
    first_name = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('help text for first name'))
    last_name_prefix = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('help text for last name prefix'))
    last_name = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('help text for last name'))
    foaf_publications = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('help text for foaf:publications'))

    @property
    def uri(self):
        return self.foaf_person

    @property
    def foaf_name(self):
        if self.last_name_prefix:
            name = "%s %s %s" % (self.first_name,
                                 self.last_name_prefix,
                                 self.last_name)
        else:
            name = "%s %s" % (self.first_name,
                              self.last_name)
        return name

    def __unicode__(self):
        return self.foaf_name

    @classmethod
    def lowercase_underscore_name(cls):
        """Transform class name from CamelCase to lowercase_with_underscores."""
        return re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', cls.__name__).lower().strip('_')

    class Meta:
        abstract = True


class DcCreator(Person):
    class Meta:
        verbose_name = 'dc:creator'
        verbose_name_plural = 'dc:creator'


class DcContributor(Person):
    class Meta:
        verbose_name = 'dc:contributor'
        verbose_name_plural = 'dc:contributor'
