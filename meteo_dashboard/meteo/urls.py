from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/mesures/<str:type_capteur>/', views.mesures_json, name='mesures_json'),
    path('statistiques/', views.statistiques, name='statistiques'),
]
