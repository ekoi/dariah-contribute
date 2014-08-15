from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from rdflib import Literal, Namespace, Graph
from rdflib.namespace import FOAF

from dariah_contributions.models import Contribution


class MyContributionsView(ListView):
    model = Contribution

    def get_queryset(self):
        return Contribution.objects.filter(author=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyContributionsView, self).dispatch(*args, **kwargs)


class ContributionRDF(DetailView):
    model = Contribution
    content_type = 'application/xml'
    template_name = 'dariah_contributions/contribution_detail.xml'

    def get_context_data(self, **kwargs):
        context = super(ContributionRDF, self).get_context_data(**kwargs)
        # Produce the RDF data ################################################
        n = Namespace("http://dariah.eu/contributions/")
        g = Graph()

        fields = context['object'].__dict__
        for field, value in fields.items():
            g.add((n.field, FOAF.about, Literal(value)))
        rdf = g.serialize(format='pretty-xml')
        #######################################################################
        context['rdf'] = rdf
        return context


class ContributionCreate(CreateView):
    model = Contribution

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ContributionCreate, self).form_valid(form)


class ContributionUpdate(UpdateView):
    model = Contribution

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionUpdate, self).dispatch(*args, **kwargs)


class ContributionDelete(DeleteView):
    model = Contribution
    success_url = reverse_lazy('dariah_contributions:list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributionDelete, self).dispatch(*args, **kwargs)
