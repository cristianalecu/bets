from rest_framework import serializers
from restuser.models import RestUser

class RestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestUser
        fields = ('id', 'code', 'myemail', 'mypassword')
        
