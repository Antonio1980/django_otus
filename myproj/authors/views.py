# from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    
    template_name = 'authors/index.html'
