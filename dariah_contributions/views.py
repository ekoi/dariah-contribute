from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.fields.related import ManyToManyField
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

import json

from taggit.managers import TaggableManager
import autocomplete_light

from .models import Contribution, DcCreator, DcContributor
from .forms import ContributionForm


class ContributionList(ListView):
    model = Contribution
    paginate_by = 25

    def get_queryset(self):
        return Contribution.objects.published()


class MyContributions(ListView):
    model = Contribution
    paginate_by = 25

    def get_queryset(self):
        return Contribution.objects.by_author(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyContributions, self).dispatch(*args, **kwargs)


class ContributionDetail(DetailView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.published_or_by_author(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ContributionDetail, self).get_context_data(**kwargs)
        c = context['object']
        context['get_fields'] = self.get_fields(c)
        context['get_metadata_fields'] = self.get_fields(c, True)
        return context

    @staticmethod
    def get_fields(c, meta_metadata=False):
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
            # If the field is an iterable (TaggableManager or ManyToManyField)
            # format the data as a string of comma separated items.
            if isinstance(field, ManyToManyField):
                value = ", ".join(map(lambda x: str(x), value.all()))
            elif isinstance(field, TaggableManager):
                value = ", ".join(value.names())
            yield field.verbose_name, value


class ContributionRDF(DetailView):
    model = Contribution
    template_name = 'dariah_contributions/contribution_detail.xml'
    content_type = 'application/xml'

    def get_queryset(self):
        return Contribution.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ContributionRDF, self).get_context_data(**kwargs)
        context['rdf'] = self.generate_rdf(context['object'])
        return context

    @staticmethod
    def generate_rdf(contribution):
        from rdflib import URIRef, BNode, Literal, Namespace, Graph
        from rdflib import RDF as rdf                                           # http://www.w3.org/1999/02/22-rdf-syntax-ns#
        from rdflib import RDFS as rdfs                                         # http://www.w3.org/2000/01/rdf-schema#
        from rdflib import XSD as xsd                                           # http://www.w3.org/2001/XMLSchema#
        from rdflib.namespace import DC as dc                                   # http://purl.org/dc/elements/1.1               AKA :
        from rdflib.namespace import DCTERMS as dcterms                         # http://purl.org/dc/terms/
        from rdflib.namespace import FOAF as foaf                               # http://xmlns.com/foaf/0.1/                    AKA default4
        from rdflib.namespace import SKOS as skos                               # http://www.w3.org/2004/02/skos/core           AKA default3
        from rdflib.namespace import XMLNS as xmlns                             # http://www.w3.org/XML/1998/namespace          AKA xml


        # Add additional namespaces
        sioc = Namespace("http://rdfs.org/sioc/ns#")                            # AKA default2
        vcard = Namespace("http://www.w3.org/2006/vcard/ns#")                   # AKA default1

        # Start the graph and bind a few prefix, namespace pairs for more readable output
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

        return g.serialize(format='pretty-xml')


###############################################################################
# FORMS VIEWS
###############################################################################
class ContributionCreate(SuccessMessageMixin, CreateView):
    model = Contribution
    form_class = ContributionForm
    success_message = _("Contribution was created successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ContributionCreate, self).form_valid(form)


class ContributionUpdate(SuccessMessageMixin, UpdateView):
    model = Contribution
    form_class = ContributionForm
    success_message = _("Contribution was updated successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.has_owner(request.user):
            raise PermissionDenied
        return super(ContributionUpdate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ContributionUpdate, self).get_context_data(**kwargs)
        c = context['object']
        context['get_readonly_fields'] = self.get_readonly_fields(c)
        return context

    def get_readonly_fields(self, c):
        """An iterable with the field names and values (in the correct order)
        of the read_only fields to be rendered in the template.
        """
        for x in self.form_class.readonly_fields:
            field = c.__class__._meta.get_field(x)
            value = getattr(c, x)
            yield field.verbose_name, value


class ContributionPublish(DetailView):
    model = Contribution
    success_message = _("Contribution was published successfully.")
    error_message = _("Something went wrong while publishing the contribution.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionPublish, self).dispatch(*args, **kwargs)

    def action(self):
        self.object.is_published = True
        self.object.save()
        return True

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if user has permission to publish item
        if not self.object.has_owner(request.user):
            raise PermissionDenied
        # Publish the item
        if self.action():
            # Set the successmessage
            messages.success(self.request, self.success_message)
        else:
            messages.error(self.request, self.error_message)
        # Redirect to original page
        if request.META.get('HTTP_REFERER'):
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ContributionUnpublish(ContributionPublish):
    success_message = _("Contribution was unpublished successfully.")
    error_message = _("Something went wrong while unpublishing the contribution.")

    def action(self):
        self.object.is_published = False
        self.object.save()
        return True


class ContributionDelete(DeleteView):
    model = Contribution
    success_url = reverse_lazy('dariah_contributions:list')
    success_message = _("Contribution was deleted successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.has_owner(request.user):
            raise PermissionDenied
        return super(ContributionDelete, self).get(self, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(success_url)


###############################################################################
# dc:creator & dc:contributor views
###############################################################################
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)

    NOTE: this class needs to be updated when Django 1.7 is used:
    https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-editing/
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        data = {
            'pk': self.object.pk,
            'name': str(self.object),
        }
        if self.success_message:
            messages.success(self.request, self.success_message % (data['name']))
        if self.request.is_ajax():
            data['django_messages'] = render_to_string('bootstrap3/messages.html', {}, RequestContext(self.request))
            return self.render_to_json_response(data)
        return response


class DcCreatorCreate(AjaxableResponseMixin, autocomplete_light.CreateView):
    model = DcCreator
    success_message = _("dc:creator %s was created successfully.")
    success_url = reverse_lazy('dariah_contributions:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DcCreatorCreate, self).dispatch(*args, **kwargs)


class DcContributorCreate(AjaxableResponseMixin, autocomplete_light.CreateView):
    model = DcContributor
    success_message = _("dc:contributor %s was created successfully.")
    success_url = reverse_lazy('dariah_contributions:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DcContributorCreate, self).dispatch(*args, **kwargs)
