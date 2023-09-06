from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Job

# Create your views here.
class HomePageView(ListView):
    model = Job 
    template_name = 'home.html' 

class JobsDetailView(DetailView):
    model = Job 
    template_name = 'job_detail.html'
    