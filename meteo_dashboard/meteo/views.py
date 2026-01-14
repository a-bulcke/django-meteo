from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from datetime import timedelta
from .models import Capteur, Mesure
import json
 
def dashboard(request):
    """Affiche le dashboard avec les données actuelles"""
    capteurs = Capteur.objects.all()
    
    # Récupérer la dernière mesure de température
    mesure_temp = Mesure.objects.filter(
        capteur__type_capteur='temperature'
    ).order_by('date_mesure').first()
    
    # TODO : Récupérer les dernières mesures de pression et humidité
    
    mesures_actuelles = {}
    if mesure_temp:
        mesures_actuelles['temperature'] = {
            'valeur': mesure_temp.valeur,
            'date': mesure_temp.date_mesure,
        }
    
    # TODO : Ajouter les mesures de pression et humidité au dictionnaire
    
    context = {
        'capteurs': capteurs,
        'mesures_actuelles': mesures_actuelles,
    }
    return render(request, 'meteo/dashboard.html', context)
 
 
def statistiques(request):
    """Affiche les statistiques sur les dernières 24 heures"""
    depuis = timezone.now() - timedelta(hours=24)
    
    stats = {}
    
    # Statistiques pour la température
    mesures_temp = Mesure.objects.filter(
        capteur__type_capteur='temperature',
        date_mesure__gte=depuis
    ).values_list('valeur', flat=True)
    
    if mesures_temp:
        stats['temperature'] = {
            'min': min(mesures_temp),
            'max': max(mesures_temp),
            'nombre': len(mesures_temp),
        }
    
    # TODO : Ajouter les statistiques pour pression (type_capteur='pression')
    # Utiliser la même structure que pour la température
    # stats['pression'] = { ... }
    
    # TODO : Ajouter les statistiques pour humidité (type_capteur='humidite')
    # Utiliser la même structure que pour la température
    # stats['humidite'] = { ... }
    
    context = {
        'stats': stats,
    }
    return render(request, 'meteo/statistiques.html', context)
 
 
@require_http_methods(["GET"])
def mesures_json(request, type_capteur):
    """Retourne les mesures au format JSON pour les graphiques"""
    
    # Vérifier que le type_capteur est valide
    types_valides = ['temperature']  # TODO : Ajouter 'pression' et 'humidite'
    
    if type_capteur not in types_valides:
        return JsonResponse({'erreur': 'Type de capteur invalide'}, status=400)
    
    # Récupérer les mesures des dernières 24 heures
    depuis = timezone.now() - timedelta(hours=24)
    
    mesures = Mesure.objects.filter(
        capteur__type_capteur=type_capteur,
        date_mesure__gte=depuis
    ).order_by('date_mesure').values(
        'valeur', 'date_mesure', 'capteur__nom'
    )
    
    donnees = [
        {
            'timestamp': m['date_mesure'].isoformat(),
            'valeur': m['valeur'],
            'capteur': m['capteur__nom'],
        }
        for m in mesures
    ]
    
    return JsonResponse({'donnees': donnees})
