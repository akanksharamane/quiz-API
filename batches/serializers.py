from rest_framework import serializers
from .models import Batches
from courses.serializers import CoursesSerializer

class BatchesSerializer(serializers.ModelSerializer):
    courseId_id = serializers.IntegerField(write_only=True)
    courses = CoursesSerializer(read_only=True)

    class Meta:
        model=Batches

        fields='__all__'
        read_only_fields=['id']

    #add custom validator

    def validate(self,data):
        if(len(data['batchType'])) == 0:
            raise serializers.ValidationError({'error':"BatchType should not be empty"})
        return data