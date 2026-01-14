from django.contrib import admin
from .models import Capteur, Mesure
 
@admin.register(Capteur)
class CapteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_capteur', 'date_creation')
    list_filter = ('type_capteur', 'date_creation')
    search_fields = ('nom',)
    readonly_fields = ('date_creation',)
 
 
@admin.register(Mesure)
class MesureAdmin(admin.ModelAdmin):
    list_display = ('capteur', 'valeur', 'date_mesure')
    list_filter = ('capteur__type_capteur', 'date_mesure')
    search_fields = ('capteur__nom',)
    readonly_fields = ('date_mesure',)
    date_hierarchy = 'date_mesure'
