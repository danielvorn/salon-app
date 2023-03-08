from rest_framework import serializers
from salonapp.models import Salon


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ['id', 'name', 'address']
