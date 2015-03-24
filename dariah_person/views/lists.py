from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from ..models import Person


class MyPersons(ListView):
    model = Person
    paginate_by = 10

    def get_queryset(self):
        return Person.objects.filter()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyPersons, self).dispatch(*args, **kwargs)