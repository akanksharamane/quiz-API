from rest_framework import serializers
from .models import Batches
from courses.serializers import CoursesSerializer

class BatchesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Batches

        fields='__all__'
        read_only_fields=['id']

    #add custom validator

    def validate(self, data):
        if(len(data['batchType'])) == 0:
            raise serializers.ValidationError({'error':"batchType should not be empty"})
        return data