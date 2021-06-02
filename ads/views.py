# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Ad

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class HomePage(ListView):
    #ListView - type of page with list of models objects.
    model = Ad
    template_name = 'index.html'
    context_object_name = 'all_ads_list' #rename model for more usable using

class AdDetail(DetailView):
    model = Ad
    template_name = 'detail.html'
