from rest_framework import serializers 

from jobs.models import Job 

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('image', 'summary')