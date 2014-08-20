from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext as _

from rdflib import Literal, Namespace, Graph
from rdflib.namespace import FOAF

from dariah_contributions.models import Contribution


class ContributionList(ListView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.published()


class MyContributions(ListView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.by_author(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyContributions, self).dispatch(*args, **kwargs)


class ContributionDetail(DetailView):
    model = Contribution

    def get_queryset(self):
        return Contribution.published.all()


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


class ContributionCreate(SuccessMessageMixin, CreateView):
    model = Contribution
    success_message = _("{model} was created successfully.").format(model=model.__name__)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ContributionCreate, self).form_valid(form)


class ContributionUpdate(SuccessMessageMixin, UpdateView):
    model = Contribution
    success_message = _("{model} was updated successfully.").format(model=model.__name__)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionUpdate, self).dispatch(*args, **kwargs)


class ContributionDelete(DeleteView):
    model = Contribution
    success_url = reverse_lazy('dariah_contributions:list')
    success_message = _("{model} was deleted successfully.").format(model=model.__name__)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionDelete, self).dispatch(*args, **kwargs)
