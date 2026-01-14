from django.db import models

# Create your models here.
from django.db import models
 
class Capteur(models.Model):
    """Modèle pour les capteurs"""
    nom = models.CharField(max_length=100, unique=True)
    type_capteur = models.CharField(
        max_length=20,
        choices=[
            ('temperature', 'Température'),
            # TODO : Ajouter les choix 'pression' et 'humidite'
        ]
    )
    topic_mqtt = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.nom} - {self.get_type_capteur_display()}"
 
    class Meta:
        verbose_name = "Capteur"
        verbose_name_plural = "Capteurs"
 
 
class Mesure(models.Model):
    """Modèle pour les mesures des capteurs"""
    capteur = models.ForeignKey(Capteur, on_delete=models.CASCADE)
    valeur = models.FloatField()
    date_mesure = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.capteur.nom}: {self.valeur}{self.unite}"
 
    class Meta:
        verbose_name = "Mesure"
        verbose_name_plural = "Mesures"
        ordering = ['-date_mesure']
