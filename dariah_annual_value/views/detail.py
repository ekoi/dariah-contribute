from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import BaseDetailView, SingleObjectTemplateResponseMixin
from django.views.generic.list import ListView
from django.template import Context, Template

from ..models import AnnualValue
   
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

