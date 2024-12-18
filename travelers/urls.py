from django.urls import path
from travelers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-trips/', views.all_trips, name='all_trips'),
    path('trips/create/', views.create_trip, name='create_trip'),
    path('trips/<int:trip_pk>/details/', views.trip_details, name='trip_details'),
    path('trips/<int:trip_pk>/edit/', views.edit_trip, name='edit_trip'),
    path('trips/<int:trip_pk>/delete/', views.delete_trip, name='delete_trip'),
    path('traveler/create/', views.create_traveler, name='create_traveler'),
    path('traveler/details/', views.traveler_details, name='traveler_details'),
    path('traveler/edit/', views.edit_traveler, name='edit_traveler'),
    path('traveler/delete/', views.delete_traveler, name='delete_traveler'),
]

LOGIN_URL = '/'
