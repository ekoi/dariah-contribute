from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView

from ..forms import AnnualValueForm
from ..models import AnnualValue


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
    