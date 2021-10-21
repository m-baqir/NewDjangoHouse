from django.shortcuts import render
from .models import Listing
import requests
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('Date')
    return render(request, "index.html", {'listings': listings})


def TorontoMapApi(request):
    response = requests.get(
        'https://ckan0.cf.opendata.inter.prod-toronto.ca/ne/api/3/action/datastore_search?resource_id=a083c865-6d60-4d1d-b6c6-b0c8a85f9c15').json
    return render(request, 'template.html', {
        'title': 'api Test',
        'api': "geojson",
        'response': response
    })


def Neighbourhoods(request):
    return render(request, "template.html", {
        "title": "List of Toronto Neighbourhoods",
    })


def pivot(request):
    return render(request, 'pivot.html')
