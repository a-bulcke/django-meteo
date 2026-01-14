from django.core.management.base import BaseCommand
from meteo.mqtt_client import meteoMQTTClient

class Command(BaseCommand):
    help = 'Démarre le client MQTT pour collecter les données météo'

    def handle(self, *args, **options):
        client = meteoMQTTClient()
        client.start()