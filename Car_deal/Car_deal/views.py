from django.shortcuts import render
from carmodel.models import CarModel
from brandmodel.models import BarndModel

def home(request, model_slug=None):
    data = CarModel.objects.all()
    brand = BarndModel.objects.all()  # Fetch all brands regardless of whether model_slug is provided
    if model_slug is not None:
        car_brand = BarndModel.objects.filter(slug=model_slug).first()  # Filter by slug and get the first result
        if car_brand:
            data = CarModel.objects.filter(brand=car_brand)  # Filter cars by the specified brand if it exists

    return render(request, 'home.html', {'data': data, 'brand_name': brand})



