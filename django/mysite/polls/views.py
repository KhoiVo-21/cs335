from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from polls.models import *

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = {
        'latest_poll_list': latest_poll_list,
    }
    # output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse("You're looking at pool %s." % poll_id)
    
def results(request, poll_id):
    return HttpResponse("results of pool %s." % poll_id)
    
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)