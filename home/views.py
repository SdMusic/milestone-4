from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def index(request):
    """ View returning index page"""

    return render(request, 'home/index.html')
