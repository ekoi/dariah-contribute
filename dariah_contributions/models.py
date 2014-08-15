from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from pycountry import languages as l

from django.contrib.auth import get_user_model
User = get_user_model()


# Managers
class PublishedContributionsManager(models.Manager):
    """Filters out all unpublished items and items with a publication date in the future"""
    def get_query_set(self):
        return super(PublishedContributionsManager, self).get_query_set() \
            .filter(is_published=True) \
            .filter(published_on__lte=timezone.now())


class Contribution(models.Model):
    # CHOICES Definitions #####################################################
    DCTERMS_ABSTRACT_LANG_CHOICES = filter(lambda x: x[0] and x[1],
                                           map(lambda x: (getattr(x, 'alpha2', None),
                                                          getattr(x, 'name', None)),
                                               l))
    # Metadata fields #########################################################
    #dc_type
    #vcard_category
    dc_identifier = models.AutoField(
        verbose_name=_("dc:identifier"),
        primary_key=True)
    dc_title = models.CharField(
        verbose_name=_("dc:title"),
        max_length=100)
    dc_date = models.DateTimeField(
        verbose_name=_("dc:date"),
        default="2014-01-01")
    dc_relation = models.CharField(
        verbose_name=_("dc:relation"),
        max_length=200,
        blank=True)
    #vcard_logo
    dc_publisher = models.CharField(
        verbose_name=_("dc:publisher"),
        max_length=200,
        blank=True)
    #dcterms_spatial
    dc_coverage = models.CharField(
        verbose_name=_("dc:coverage"),
        max_length=200,
        blank=True)
    #vcard_organization
    dc_subject = models.CharField(
        verbose_name=_("dc:subject"),
        max_length=50,
        blank=True)
    dcterms_abstract = models.TextField(
        verbose_name=_("dcterms:abstract"),
        blank=True)
    dcterms_abstract_lang = models.CharField(
        verbose_name=_("dcterms:abstract lang"),
        max_length=2,
        choices=DCTERMS_ABSTRACT_LANG_CHOICES,
        default='en')
    dc_description = models.TextField(
        verbose_name=_("dc:description"),
        blank=True)
    #sioc_topic
    #sioc_has_scope
    dc_creator = models.ManyToManyField(
        'DcCreator',
        blank=True,
        null=True,
        verbose_name=_("dc:creator"))
    dc_contributor = models.ManyToManyField(
        'DcContributor',
        blank=True,
        null=True,
        verbose_name=_("dc:contributor"))

    # Meta-Metadata fields ####################################################
    author = models.ForeignKey(User, editable=False)
    is_published = models.BooleanField(default=False, )
    published_on = models.DateTimeField(
        verbose_name=_('published on'),
        blank=True,
        null=True)
    last_modified_on = models.DateTimeField(
        verbose_name=_('last modified on'),
        default=timezone.now)

    # Managers ################################################################
    objects = models.Manager()
    published = PublishedContributionsManager()

    def __unicode__(self):
        return self.dc_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-published_on', ]
        get_latest_by = 'published_on'
        verbose_name = _('contribution')
        verbose_name_plural = _('contributions')

    def save(self, *args, **kwargs):
        """Add publication date is now if published is True but no date was selected"""
        if self.is_published and not self.published_on:
            self.published_on = timezone.now()
        """ Always add last_modified_on date """
        self.last_modified_on = timezone.now()
        super(Contribution, self).save(*args, **kwargs)


class Person(models.Model):
    foaf_person = models.CharField(max_length=50, blank=True)
    foaf_name = models.CharField(max_length=50, blank=True)
    foaf_publications = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.foaf_name

    class Meta:
        abstract = True


class DcCreator(Person):
    pass


class DcContributor(Person):
    pass
