from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from rdflib import Literal, Namespace, Graph
from rdflib.namespace import FOAF

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
        context['many2many_fields'] = {
            'skos_preflabel_technique': ', '.join(map(lambda x: str(x),
                                                      c.skos_preflabel_technique.all())),
        }
        return context


class ContributionRDF(DetailView):
    model = Contribution
    template_name = 'dariah_contributions/contribution_detail.xml'
    content_type = 'application/xml'

    def get_queryset(self):
        return Contribution.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ContributionRDF, self).get_context_data(**kwargs)
        # Produce the RDF data ################################################
        n = Namespace("http://dariah.eu/contributions/")
        g = Graph()

        for field, value in context['object'].attrs():
            g.add((n.field, FOAF.about, Literal(value)))
        rdf = g.serialize(format='pretty-xml')
        #######################################################################
        context['rdf'] = rdf
        return context


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


class DcCreatorCreate(SuccessMessageMixin, CreateView):
    model = DcCreator
    success_message = _("dc:creator was created successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DcCreatorCreate, self).dispatch(*args, **kwargs)


class DcContributorCreate(SuccessMessageMixin, CreateView):
    model = DcContributor
    success_message = _("dc:contributor was created successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DcContributorCreate, self).dispatch(*args, **kwargs)
