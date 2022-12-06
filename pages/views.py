from django.shortcuts import render
from .models import Team
from django.shortcuts import get_object_or_404
from cars.models import car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car.objects.order_by('-created_date').all()
    # search_fields = car.objects.values('model', 'city', 'year', 'body_style')
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields': search_fields,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
