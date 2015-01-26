from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect

from django.contrib import messages

# Create your views here.

from .forms import SignUpForm
from django.db.transaction import commit

def join(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'We will in touch.')
        return HttpResponseRedirect('/signups/thank-you/')
    
    return render_to_response("signup.html", 
                              locals(),
                              context_instance=RequestContext(request))
    
def thankyou(request):
    print "hello"
    return render_to_response("signups/thankyou.html", 
                              locals(),
                              context_instance=RequestContext(request))
   