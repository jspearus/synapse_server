from rest_framework import serializers
from .models import *

class ClientStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientStats 
        fields = ('id', 'client_name', 'auto_mode', 'stats', 
                  'status')