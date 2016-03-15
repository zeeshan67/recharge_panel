from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
# Create your views here.


def index(request):
    request.session.set_expiry(3600)
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html',"aUrl":"/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })
    request.session['role'] = 'user'
    template = loader.get_template('commons/index.html')
    return HttpResponse(template.render(context_data))

def view_plan(request):
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html',"aUrl":"/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })
    template = loader.get_template('commons/single.html')
    return HttpResponse(template.render(context_data))