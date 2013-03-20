from django.shortcuts import render_to_response
from django.http import Http404
import datetime

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
    