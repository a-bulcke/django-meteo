import paho.mqtt.client as mqtt
import os
import django
import sys
import logging
from datetime import datetime
 
# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meteo_config.settings')
django.setup()
 
from meteo.models import Capteur, Mesure
from dotenv import load_dotenv
 
# Charger les variables d'environnement
load_dotenv()
 
# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
 
# Configuration MQTT
MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_USERNAME = os.getenv('MQTT_USERNAME', '')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', '')
 
# Topics MQTT
TOPICS = [
    ('meteo/temperature', 'temperature'),
]
 
# Mapping topics → capteurs
CAPTEURS_CONFIG = {
    'meteo/temperature': {
        'type': 'temperature',
        #'unite': 'C',
        'nom': 'Capteur Température',
    },
}
 
 
class meteoMQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id='django_meteo')
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        
        if MQTT_USERNAME:
            self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
 
    def on_connect(self, client, userdata, flags, rc):
        """Callback de connexion"""
        if rc == 0:
            logger.info(f"✅ Connecté au broker MQTT ({MQTT_BROKER}:{MQTT_PORT})")
            # S'abonner aux topics
            for topic, _ in TOPICS:
                client.subscribe(topic)
                logger.info(f"📡 Abonné au topic: {topic}")
        else:
            logger.error(f"❌ Erreur de connexion (code: {rc})")
 
    def on_disconnect(self, client, userdata, rc):
        """Callback de déconnexion"""
        if rc != 0:
            logger.warning(f"⚠️ Déconnexion inattendue (code: {rc})")
        else:
            logger.info("🔌 Déconnexion gracieuse")
 
    def on_message(self, client, userdata, msg):
        """Callback de réception de message"""
        topic = msg.topic
        
        try:
            # Récupérer la valeur
            valeur = float(msg.payload.decode())
            
            if topic not in CAPTEURS_CONFIG:
                logger.warning(f"⚠️ Topic inconnu: {topic}")
                return
 
            config = CAPTEURS_CONFIG[topic]
            
            # Récupérer ou créer le capteur
            capteur, created = Capteur.objects.get_or_create(
                topic_mqtt=topic,
                defaults={
                    'nom': config['nom'],
                    'type_capteur': config['type'],
                    #'localisation': 'Local',
                }
            )
 
            # Créer la mesure
            mesure = Mesure.objects.create(
                capteur=capteur,
                valeur=valeur,
                #unite=config['unite'],
            )
 
            logger.info(
                f"✔️ Mesure enregistrée - {capteur.nom}: "
                #f"{valeur}{config['unite']} à {mesure.date_mesure.strftime('%H:%M:%S')}"
            )
 
        except ValueError as e:
            logger.error(f"❌ Erreur de conversion de valeur: {msg.payload}")
        except Exception as e:
            logger.error(f"❌ Erreur lors du traitement du message: {str(e)}")
 
    def start(self):
        """Démarre le client MQTT"""
        try:
            logger.info(f"🚀 Démarrage du client MQTT...")
            self.client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
            self.client.loop_forever()
        except Exception as e:
            logger.error(f"❌ Erreur: {str(e)}")
            sys.exit(1)
 
 
if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("Dashboard Météo - Client MQTT")
    logger.info("=" * 50)
    
    mqtt_client = meteoMQTTClient()
    mqtt_client.start()

