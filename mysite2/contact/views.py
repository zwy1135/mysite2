from django.core.mail import send_mail
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,Http404,HttpResponseRedirect
from forms import ContactForm

def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@aaa.com']
                )
            return HttpResponseRedirect('/contact/thanks/')
    else:form = ContactForm(initial={'subject':'haha'})        
    return render_to_response('contact_form.html',
        {'form': form},context_instance=RequestContext(request))