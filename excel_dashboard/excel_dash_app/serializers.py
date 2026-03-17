from rest_framework import serializers

from .models import filemodel , brand


class fileserializer(serializers.ModelSerializer):
    class Meta:
        model = filemodel
        fields = '__all__'
    
class brandserializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = '__all__'