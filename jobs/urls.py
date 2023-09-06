from django.urls import path 
from .views import HomePageView, JobsDetailView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jobs/<int:pk>/', JobsDetailView.as_view(), name='job_detail'),
] 