from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import UpdateView
from django.core.exceptions import PermissionDenied

from ..forms import AnnualValueForm
from ..models import AnnualValue
from dariah_inkind.models import Contribution

class AnnualValueUpdate(SuccessMessageMixin, UpdateView):
    model = AnnualValue
    form_class = AnnualValueForm
    success_message = _("Annual value was updated successfully.")
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnnualValueUpdate, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AnnualValueUpdate, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnualValueUpdate, self).get_context_data(**kwargs)
        mycontributes = Contribution.objects.by_author(self.request.user)
        context['form'].fields['inkind'].queryset = mycontributes
        return context

   

