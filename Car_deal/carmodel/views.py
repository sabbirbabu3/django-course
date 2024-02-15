from django.shortcuts import redirect, render
from django.views.generic import DetailView
from . import models
from . import forms
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect




class CardetailsView(DetailView):
    model = models.CarModel
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        form = forms.CommentsForm(request.POST)
        if form.is_valid():
            carmodel = self.get_object()
            new_comment = form.save(commit=False)
            new_comment.car_model = carmodel
            new_comment.save()
            return redirect('details', id=carmodel.id)
        else:
            # If form is not valid, re-render the details page with the form and existing comments
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carmodel = self.object
        comments = models.comments.objects.filter(car_model=carmodel)
        form = forms.CommentsForm()
        total_cars_count = models.CarModel.objects.count() 
        context['comments'] = comments
        context['comments_form'] = form
        context['total_cars_count'] = total_cars_count
        return context
    
def Buycar(request, id):
    car = models.CarModel.objects.get(pk=id) 

    # Call the method to get the count value
    car_count = car.brand.car_count()

    if car_count > 0:
        car.brand.car_count -= 1
        car.brand.save()

        # Create a new instance of CarModel as part of the buying process
        buying = models.CarModel.objects.create(
            car_name=car.car_name,
            car_price=car.car_price,
            brand=car.brand,
            author=request.user,
            image=car.image,
            details=car.details,
        )

        messages.success(request, 'Car purchased successfully')
    else:
        messages.error(request, 'This car is not available in our stock')

    return redirect('profile')
