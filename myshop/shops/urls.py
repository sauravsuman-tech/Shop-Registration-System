from django.urls import path
from . import views

urlpattern = [
    path('register/', views.register_shop, name = 'register_shop'),
    path('serach/', views.search_naerby_shops, name = 'search_naeryby_shops'),
]