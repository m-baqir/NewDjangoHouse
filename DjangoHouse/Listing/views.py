from django.shortcuts import render, get_object_or_404
from .models import Listing
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection  import test_train_split
from sklearn.linear_model import LinearRegression
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
    return render(request,'pivot.html');

# Housing Detail
def detail(request, id=None):
    id = request.form.get('id')
    house =  get_object_or_404(Listing, id=id)
    context={
        'house': house,
    }
    return render(request, "detail.html", context)

def Predict(request):
    data = pd.read_csv('houseprice.csv')
    X = data.drop('price',axis=1)
    Y = data["price"]
    X_Train , X_Test , Y_Train , Y_Test = train_test_split(X , Y , test_size= .30)
    model = LinearRegression()
    fit = model.fit(X_Train,Y_Train)

    area = float(request.GET['area'])
    age = float(request.GET['age'])
    rooms = float(request.GET['rooms'])
    population = float(request.GET['population'])
    price = fit.predict(np.array([area,age,rooms,population]))
    price = "The predicted price is "+str(round(price[0]))
    return render(request , "predict.html",{"response":price})
