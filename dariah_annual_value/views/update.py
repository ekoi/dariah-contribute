from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import UpdateView
from django.core.exceptions import PermissionDenied

from ..forms import AnnualValueForm
from ..models import AnnualValue

class AnnualValueUpdate(SuccessMessageMixin, UpdateView):
    model = AnnualValue
    print '============='
    print model.inkind
    print '============='
    form_class = AnnualValueForm
    success_message = _("Contribution was updated successfully.")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnnualValueUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AnnualValueUpdate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnualValueUpdate, self).get_context_data(**kwargs)
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
   

