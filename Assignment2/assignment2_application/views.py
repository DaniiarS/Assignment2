from django.shortcuts import render
from django.http import HttpResponse
from .models import Record, Disease, DiseaseType, Country
# Create your views here.

posts = [
    {
        'author': 'DaniiarS',
        'title': 'Assignment2 Title 1',
        'content': 'This is the content of the Assignment2 1',
        'date_posted': 'November 21, 2022'
    },
    {
        'author': 'Charlotte Billei',
        'title': 'Assignment2 Title 2',
        'content': 'This is the content of the Assignment2 2',
        'date_posted': 'November 20, 2022'
    }
]
def home( request ):
    context = {
        'posts' : Disease.objects.all(),
        'title' : 'Home'
    }

    return render( request, 'assignment2_application/home.html', context )

def about( request ):
    title_dict = {
        'title' : 'About',
        'd_types': DiseaseType.objects.all()
    }
    return render( request, 'assignment2_application/about.html', title_dict )

def countries( request ):
    context = {
        'countries': Country.objects.all(),
    }

    return render( request, 'assignment2_application/countries.html', context )