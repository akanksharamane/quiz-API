from rest_framework  import serializers
from .models import Enquiry

class EnquirySeriaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry
        fields ='__all__'
        read_only_fields = ['id']
        
    #add custom validator
    def validate(self,data):
        if(len(data['name'])) == 0:
            raise serializers.ValidationError({'error':"Name should not be empty"})
        return data