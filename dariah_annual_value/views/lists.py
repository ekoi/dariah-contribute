from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from ..models import AnnualValue


class MyAnnualValues(ListView):
    model = AnnualValue
    paginate_by = 10

    def get_queryset(self):
        return AnnualValue.objects.by_author(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyAnnualValues, self).dispatch(*args, **kwargs)