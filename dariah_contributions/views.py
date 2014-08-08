from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import RDF, FOAF


from dariah_contributions.models import Contribution
from dariah_contributions.forms import ContributionForm

def index(request):
    return render(request, 'dariah_contributions/index.html')

class list_view(generic.ListView):
    template_name = 'dariah_contributions/list.html'
    context_object_name = 'contribution_list'

    def get_queryset(self):
        return Contribution.objects.order_by('-publish_date')


##def list_view_own(request):
##    contribution_list = Contribution.objects.filter(contributor="Vesa").order_by('-publish_date')
##    return object_list(request, queryset=contribution_list)

class detail_view(generic.DetailView):
    model = Contribution
    template_name = 'dariah_contributions/detail.html'

def detail_view_rdf(request, pk):
    try:
        contribution = Contribution.objects.get(pk=pk)
        n = Namespace("http://dariah.eu/contributions/")
        g = Graph()

        fields= contribution.__dict__
        for field, value in fields.items():
            g.add( ( n.field, FOAF.about, Literal(value) ) )
        rdf = g.serialize(format='pretty-xml')
    except:
        contribution = None
        rdf = None
        
    return render(request, 'dariah_contributions/detail_rdf.html', {'contribution': contribution, 'rdf': rdf})
        
@login_required
def contribution(request, contribution_id):
    try:
        contribution = Contribution.objects.get(pk=contribution_id)
    except:
        contribution = None
    form = ContributionForm(instance=contribution)
    
    if request.method == 'POST':
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            # can this be done otherwise?
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.modify_date = datetime.now()
            obj.save()
            return HttpResponseRedirect('/dariah_contributions/list/')

    return render(request, 'dariah_contributions/contribution.html', {'form': form})

def dariah_logout(request):
    logout(request)
    return HttpResponseRedirect('/dariah_contributions/')


