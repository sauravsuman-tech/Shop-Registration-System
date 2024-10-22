import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from dotenv import load_dotenv

from rest_framework import serializers
from models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']