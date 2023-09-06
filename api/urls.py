from django.urls import path 

from .views import JobApiView

urlpatterns = [
    path('', JobApiView.as_view()), 
]
