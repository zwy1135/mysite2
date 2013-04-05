from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,Http404,HttpResponseRedirect
from books.models import Book
import datetime
from django.core.mail import send_mail


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except:raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})
    
def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('meta.html',{'values':values})
      
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_form.html',{'errors':errors})
 
#@csrf_exempt 
