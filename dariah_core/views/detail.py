from django.contrib.sites.models import Site
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField, ForeignKey
from django.http import HttpResponse
from django.template import Context, Template
from django.utils.translation import ugettext as _
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin

from taggit.managers import TaggableManager

from ..models import Contribution


class ContributionRDFResponseMixin(object):
    def render_to_response(self, context):
        "Returns a RDF response containing 'context' as payload"
        return self.get_rdf_response(self.convert_context_to_rdf(context, 'xml'))

    def get_rdf_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                            content_type='application/xml',
                            **httpresponse_kwargs)

    def convert_context_to_rdf(self, context, rdf_format='pretty-xml'):
        "Convert the context dictionary into a RDF object"
        c = context['object']
        site = Site.objects.get_current()

        from rdflib import URIRef, BNode, Literal, Namespace, Graph
        from rdflib import RDF as rdf                                           # http://www.w3.org/1999/02/22-rdf-syntax-ns#
        from rdflib import RDFS as rdfs                                         # http://www.w3.org/2000/01/rdf-schema#
        from rdflib import XSD as xsd                                           # http://www.w3.org/2001/XMLSchema#
        from rdflib.namespace import DC as dc                                   # http://purl.org/dc/elements/1.1
        from rdflib.namespace import DCTERMS as dcterms                         # http://purl.org/dc/terms/
        from rdflib.namespace import FOAF as foaf                               # http://xmlns.com/foaf/0.1/
        from rdflib.namespace import SKOS as skos                               # http://www.w3.org/2004/02/skos/core
        from rdflib.namespace import XMLNS as xmlns                             # http://www.w3.org/XML/1998/namespace

        # Add additional namespaces
        sioc = Namespace("http://rdfs.org/sioc/ns#")                            # AKA default2
        vcard = Namespace("http://www.w3.org/2006/vcard/ns#")                   # AKA default1

        ### PREPARE THE GRAPH #################################################
        # Start the graph and bind a few prefix, namespace pairs for more
        # readable output
        g = Graph()
        g.bind("rdf", rdf)
        g.bind("rdfs", rdfs)
        g.bind("xsd", xsd)
        g.bind("dc", dc)
        g.bind("dcterms", dcterms)
        g.bind("foaf", foaf)
        g.bind("skos", skos)
        g.bind("xmlns", xmlns)
        g.bind("sioc", sioc)
        g.bind("vcard", vcard)

        # Declare the item
        this_contribution = URIRef(c.get_absolute_url())

        # Add skos:preflabel BNodes to the graph and item / skos:preflabel
        if c.skos_preflabel_activity.count():
            tadirah_activity = BNode()
            g.add((tadirah_activity, rdf.type, skos.Concept))
            g.add((this_contribution, sioc.topic, tadirah_activity))
        if c.skos_preflabel_discipline.count():
            discipline = BNode()
            g.add((discipline, rdf.type, skos.Concept))
            g.add((this_contribution, sioc.topic, discipline))
        if c.skos_preflabel_object.count():
            tadirah_object = BNode()
            g.add((tadirah_object, rdf.type, skos.Concept))
            g.add((this_contribution, sioc.topic, tadirah_object))
        if c.skos_preflabel_technique.count():
            tadirah_technique = BNode()
            g.add((tadirah_technique, rdf.type, skos.Concept))
            g.add((this_contribution, sioc.topic, tadirah_technique))
        if c.skos_preflabel_vcc.count():
            tadirah_vcc = BNode()
            g.add((tadirah_vcc, rdf.type, skos.Concept))
            g.add((this_contribution, sioc.has_scope, tadirah_vcc))

        #######################################################################
        # Add tripples about the item to the graph
        g.add((this_contribution, dc.type, URIRef(u'http://purl.org/ontology/bibo/Webpage')))
        g.add((this_contribution, vcard.category, URIRef(u'http://data.dariah.eu/vocabulary/item/contribution')))

        if c.dc_identifier:
            g.add((this_contribution, dc.identifier, URIRef(c.get_absolute_url())))
        if c.dc_title:
            g.add((this_contribution, dc.title, Literal(c.dc_title, lang=u'en')))
        if c.dc_date:
            g.add((this_contribution, dc.date, Literal(u'%s-01-01' % c.dc_date, lang=u'en')))
        if c.dc_relation:
            g.add((this_contribution, dc.relation, URIRef(c.dc_relation)))
        if c.vcard_logo:
            g.add((this_contribution, vcard.logo, URIRef("%s%s" % (site.domain, c.vcard_logo.url))))
        if c.dc_publisher:
            g.add((this_contribution, dc.publisher, Literal(c.dc_publisher, lang=u'en')))
        if c.dcterms_spatial:
            g.add((this_contribution, dcterms.spatial, URIRef(c.dcterms_spatial)))
        if c.dc_coverage:
            g.add((this_contribution, dc.coverage, URIRef(c.dc_coverage.uri)))
        if c.vcard_organization:
            g.add((this_contribution, vcard.organization, Literal(c.vcard_organization, lang=u'en')))
        # Many2Many dc:subject
        for s in c.dc_subject.all():
            g.add((this_contribution, dc.subject, Literal(s, lang=u'en')))
        # EndMany2Many
        if c.dcterms_abstract_en:
            g.add((this_contribution, dcterms.abstract, Literal(c.dcterms_abstract_en, lang=u'en')))
        if c.dcterms_abstract:
            g.add((this_contribution, dcterms.abstract, Literal(c.dcterms_abstract, lang=c.dcterms_abstract_lang)))
        if c.dc_description:
            g.add((this_contribution, dc.description, Literal(c.dc_description, lang=u'en')))

        # Many2Many skos:preflabels
        for x in c.skos_preflabel_activity.all():
            g.add((tadirah_activity, skos.prefLabel, URIRef(x.uri)))
        for x in c.skos_preflabel_discipline.all():
            g.add((discipline, skos.prefLabel, URIRef(x.uri)))  # Note: URI contains 'subject' instead of 'discipline'
        for x in c.skos_preflabel_object.all():
            g.add((tadirah_object, skos.prefLabel, URIRef(x.uri)))
        for x in c.skos_preflabel_technique.all():
            g.add((tadirah_technique, skos.prefLabel, URIRef(x.uri)))
        for x in c.skos_preflabel_vcc.all():
            g.add((tadirah_vcc, skos.prefLabel, URIRef(x.uri)))
        # EndMany2Many

        # Many2Many dc:creator
        for x in c.dc_creator.all():
            creator = URIRef(x.foaf_person) if x.foaf_person else BNode()
            g.add((this_contribution, dc.creator, creator))
            g.add((creator, rdf.type, foaf.Person))
            if x.foaf_name:
                g.add((creator, foaf.name, Literal(x.foaf_name, lang=u'en')))
            if x.foaf_publications:
                g.add((creator, foaf.publications, URIRef(x.foaf_publications)))
        # EndMany2Many
        # Many2Many dc:contributor
        for x in c.dc_contributor.all():
            contributor = URIRef(x.foaf_person) if x.foaf_person else BNode()
            g.add((this_contribution, dc.contributor, contributor))
            g.add((contributor, rdf.type, foaf.Person))
            if x.foaf_name:
                g.add((contributor, foaf.name, Literal(x.foaf_name, lang=u'en')))
            if x.foaf_publications:
                g.add((contributor, foaf.publications, URIRef(x.foaf_publications)))
        # EndMany2Many

        # Return the graph as pretty XML
        return g.serialize(format=rdf_format)


class ContributionDetailMixin(BaseDetailView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.published_or_by_author(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ContributionDetailMixin, self).get_context_data(**kwargs)
        c = context['object']
        context['get_fields'] = self.get_fields(c)
        context['get_metadata_fields'] = self.get_fields(c, True)
        return context

    def get_fields(self, c, meta_metadata=False):
        """An iterable with the field names and values (in the correct order)
        of a Contribution instance to be rendered in the template.
        """
        if meta_metadata:
            fields = filter(lambda x: x[2], c.field_order)
        else:
            fields = filter(lambda x: not x[2], c.field_order)
        for x in fields:
            field = c.__class__._meta.get_field(x[0])
            value = getattr(c, x[0])
            is_safe = False
            help_text = unicode(field.help_text)
            # If the field is an iterable (TaggableManager or ManyToManyField)
            # format the data as a string of comma separated items.
            if isinstance(field, ManyToManyField):
                value = ", ".join(map(lambda x: self.link(x), value.all()))
                is_safe = True
            elif isinstance(field, TaggableManager):
                value = ", ".join(value.names())
                is_safe = True
            elif isinstance(field, ForeignKey):
                value = self.link(value)
                is_safe = True
            elif isinstance(field, ImageField):
                value = self.image(value)
                is_safe = True
            yield field.verbose_name, value, is_safe, help_text

    @staticmethod
    def link(value):
        if hasattr(value, 'uri') and getattr(value, 'uri'):
            template = Template('<a href="{{ uri }}" title="{{ value }}">{{ value }}</a>')
            context = Context({'value': str(value), 'uri': value.uri})
            return template.render(context)
        return str(value)

    @staticmethod
    def image(value):
        if hasattr(value, 'url') and getattr(value, 'url'):
            template = Template('<a href="{{ uri }}" title="vcard:logo"><img class="detail-vcard-logo" src="{{ uri }}" /></a><br/>{{ location }}: <a href="{{ uri }}" title="vcard:logo">{{ uri }}</a>')
            context = Context({'value': str(value), 'uri': value.url, 'location': _('Location')})
            return template.render(context)
        return str(value)


class ContributionRDF(ContributionRDFResponseMixin, BaseDetailView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.published_or_by_author(self.request.user)


class ContributionDetail(ContributionDetailMixin, SingleObjectTemplateResponseMixin):
    pass


class ContributionHybridDetail(ContributionDetailMixin,
                               ContributionRDFResponseMixin,
                               SingleObjectTemplateResponseMixin):

    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        http_accept = self.parse_accept_header(self.request.META.get('HTTP_ACCEPT', ""))
        if (self.request.GET.get('format', 'html') == 'xml') or \
           (http_accept.get('application/xml', 0) > http_accept.get('text/html', 0)) or \
           (http_accept.get('application/xhtml+xml', 0) > http_accept.get('text/html', 0)):
            return ContributionRDFResponseMixin.render_to_response(self, context)
        else:
            return SingleObjectTemplateResponseMixin.render_to_response(self, context)

    @staticmethod
    def parse_accept_header(accept):
        """Parse the Accept header *accept*, returning a dictionary with the
        media type as key and the q value as value. Note: media_params is not
        used.
        Original source: https://djangosnippets.org/snippets/1042/
        """
        result = {}
        for media_range in accept.split(","):
            parts = media_range.split(";")
            media_type = parts.pop(0)
            media_params = []
            q = 1.0
            for part in parts:
                (key, value) = part.lstrip().split("=", 1)
                if key == "q":
                    q = float(value)
                    media_params.append((key, value))
            result[media_type] = q
        return result
