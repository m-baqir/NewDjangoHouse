from django.shortcuts import render
from .models import Listing
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('Date')
    return render(request, "index.html", {'listings': listings})