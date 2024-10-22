from django.shortcuts import render
from rest_framework import status
from shops.models import Shop
from .utils import haversine
from shops.utils import haversine
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shops.serializers import ShopSerializer

@api_view(['POST'])
def register_shop(request):
    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_nearby_shops(request):
    user_lat = float(request.GET.get('latitude'))
    user_lon = float(request.GET.get('longitude'))

    shops = Shop.objects.all()
    shops_with_distance = []

    for shop in shops:
        distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
        shops_with_distance.append((shop, distance))

    sorted_shops = sorted(shops_with_distance, key=lambda x: x[1])

    sorted_shops_data = [{
        'name': shop.name,
        'latitude': shop.latitude,
        'longitude': shop.longitude,
        'distance': distance
    } for shop, distance in sorted_shops]

    return Response(sorted_shops_data)