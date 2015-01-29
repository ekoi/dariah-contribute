from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.template import Context, Template

from .forms import AnnualValueForm
from .models import AnnualValue


# Create your views here.
def join(request):
     
    form = AnnualValueForm(request.POST or None)
     
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'We will in touch.')
        return HttpResponseRedirect('/annual-value/thank-you/')
     
    return render_to_response("annualvalue.html", 
                              locals(),
                              context_instance=RequestContext(request))
     
# def thankyou(request):
#     print "hello"
#     return render_to_response("annual-value/thankyou.html", 
#                               locals(),
#                               context_instance=RequestContext(request))
   


class AnnualValueCreate(SuccessMessageMixin, CreateView):
    model = AnnualValue
    form_class = AnnualValueForm
    success_message = _("AnnualValue was created successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnnualValueCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnnualValueCreate, self).form_valid(form)
    
   
   
class AnnualValueDetailMixin(BaseDetailView):
    model = AnnualValue
    
    
    def get_context_data(self, **kwargs):
        context = super(AnnualValueDetailMixin, self).get_context_data(**kwargs)
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
            help_text = unicode(field.help_text)
            # If the field is an iterable (TaggableManager or ManyToManyField)
            # format the data as a string of comma separated items.
            
            yield field.verbose_name, value,help_text

    @staticmethod
    def link(value):
        if hasattr(value, 'uri') and getattr(value, 'uri'):
            template = Template('<a href="{{ uri }}" title="{{ value }}">{{ value }}</a>')
            context = Context({'value': str(value), 'uri': value.uri})
            return template.render(context)
        return str(value)


    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        return SingleObjectTemplateResponseMixin.render_to_response(self, context)
    
class AnnualValueDetail(AnnualValueDetailMixin, SingleObjectTemplateResponseMixin):
    pass


class MyAnnualValues(ListView):
    model = AnnualValue
    paginate_by = 25

    def get_queryset(self):
        return AnnualValue.objects.by_author(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyAnnualValues, self).dispatch(*args, **kwargs)