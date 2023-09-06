from rest_framework.generics import ListAPIView

from jobs.models import Job 
from .serializers import JobSerializers


# Create your views here.
class JobApiView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
