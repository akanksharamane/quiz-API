from rest_framework import serializers
from .models import Feedback


class FeedbacksSerializer(serializers.ModelSerializer):

    class Meta:
        model=Feedback

        fields='__all__'
        read_only_fields=['id']

    #add custom validator

    def validate(self,data):
        if(len(data['name'])) == 0:
            raise serializers.ValidationError({'error':"name should not be empty"})
        return data