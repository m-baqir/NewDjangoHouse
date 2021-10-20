from django.shortcuts import render, get_object_or_404
from .models import Listing
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('Date')
    return render(request, "index.html", {'listings': listings})


def pivot(request):
    return render(request, 'pivot.html')

# Housing Detail
def detail(request, id=None):
    id = request.form.get('id')
    house =  get_object_or_404(Listing, id=id)
    context={
        'house': house,
    }
    return render(request, "detail.html", context)
