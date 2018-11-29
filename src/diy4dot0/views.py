# coding: utf-8

import datetime
import json
import logging
import sys

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404 
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from wsgiref.util import FileWrapper


#from graphos.sources.simple import SimpleDataSource
#from graphos.renderers.gchart import LineChart
logger = logging.getLogger("project")


class HomePage(generic.TemplateView):
    template_name = "home.html"
            

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class Downloads(generic.TemplateView):
    template_name = "downloads.html"
    
class RegisteredDevices(generic.TemplateView):
    template_name = "registereddevices.html"

class FirstSteps(generic.TemplateView):
    template_name = "firststeps.html"
    
def downloadRelease(request,number):
    import os
    import zipfile
    import io
    
    release_filename = "diy4dot0release"+str(number)+".zip"
    release_path=os.path.join(settings.RELEASES_ROOT,release_filename)
    file_wrapper = FileWrapper(open(release_path,'rb'))
    
    response = HttpResponse(file_wrapper, content_type = "application/x-zip-compressed")
    response['Content-Length'] = os.stat(release_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % release_filename

    return response


def custom_error500_view(request):
    exceptionType= sys.exc_info()[0].__name__
    if exceptionType=='XMLException':
        exceptionDescription='FAILURE IN THE CONFIGURATION XML FILE: ' +str(sys.exc_info()[1])
    else:
        exceptionDescription='Internal server error. No more information provided for security reasons'
    return render(request,'500.html',{'exception_value': exceptionDescription})
