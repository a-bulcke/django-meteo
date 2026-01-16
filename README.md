TP : Dashboard MÚtÚo avec Django et MQTT

# Introduction

Django est un Framework Python, open-source et gratuit qui permet de crÚer un site web. Il facilite le processus de dÚveloppement en fournissant tous les outils nÚcessaires pour crÚer des sites web dynamiques.

## Objectifs de l'activitÚ

└ la fin de cette activitÚ, vous serez capable de :

* Installer et configurer Django
* Comprendre l'architecture MVT de Django
* CrÚer des modÞles de donnÚes

# Installation et Configuration Initiale

## PrÚalables

Installez d'abord :

* Python 3.8 ou supÚrieur
* pip
* Un broker MQTT (pour les tests utilisez test.mosquitto.org)
* Un Úditeur de code (VS Code)

## Installation de Django et dÚpendances

### Importer le projet

git clone https://github.com/a-bulcke/django-meteo.git

cd django\_meteo

### CrÚer un environnement virtuel

python -m venv env

Sous VSCode tapezáshift+Ctrl+P puisá:

![Create Environment dropdown](data:image/png;base64...)

Cet environnement protÞge votre projet des conflits avec d'autres bibliothÞques Python.

### Activer l'environnement

# Sur Windows :
.venv\Scripts\Activate.ps1
# Sur macOS/Linux :
source env/bin/activate

Avec VScode lÆenvironnement virtuel est automatiquement sÚlectionnÚ. Il suffit dÆouvrir un terminal dans le menu Affichage.

Vous remarquerez que le nom de l'environnement appara¯t entre parenthÞses dans votre terminal.

![](data:image/png;base64...)

### Installer les dÚpendances

pip install requirements.txt

Attendez que l'installation se termine, puis vÚrifiez que Django est correctement installÚ en tapantá:

django-admin --version

## Projet Django meteo\_dashboard

### Structure du projet

Lorsque quÆun projet Django est gÚnÚrÚ (voir Comment crÚer un projet Django), une structure de dossiers complÞte avec tous les fichiers de configuration nÚcessaires est crÚÚe.

Ci-dessous voici la structure du projet ***meteo\_dashboard***á:

meteo\_dashboard/

??? meteo\_dashboard/ # Configuration du projet

? ??? settings.py # ParamÞtres du projet

? ??? urls.py # Routage principal

? ??? asgi.py

??? meteo/ # Application mÚtÚo

? ??? models.py # ModÞles de donnÚes

? ??? views.py # Logique mÚtier

? ??? urls.py # Routage de l'app

? ??? management/ # commandes personnalisÚes

? ? ??? commands/

? ? ??? mqtt\_client.py

? ??? templates/ # Templates HTML

? ? ??? meteo/

? ? ??? base.html

? ? ??? dashboard.html

? ? ??? statistiques.html

? ??? static/ # Fichiers CSS, JS, images

? ? ??? meteo/

? ? ??? css/

? ? ? ??? style.css

? ? ? ??? dashboard.css

? ? ??? js/

? ? ??? charts.js

? ??? admin.py # Configuration admin

? ??? mqtt\_client.py # Script MQTT

??? manage.py # Outil de gestion Django

??? db.sqlite3 # Base de donnÚes

??? .env # Variables d'environnement

# Principes de fonctionnement de Django

## EcosystÞme Django

![Projet et application Django](data:image/png;base64...)

## ModÞle MVT (ModÞle-Vue-Template)

RequÛte HTTP

Gestion des URLs

**urls.py**

Gestion des vues

**views.py**

Templateá: gabarit de page

**<nom\_fichier>.html**

Gestion des donnÚes

**models.py**

RÚponse http

HTML

![](data:image/png;base64...)

Reþoit les requÛtes et rÚpond Ó lÆaide des templates

Interroge la BDD

GÞre les urls et interroge la vue correspondante

![](data:image/png;base64...)

Affiche les donnÚes

![](data:image/png;base64...)

# ExÚcution du Projet

## CrÚer un superutilisateur pour lÆadministration

python manage.py createsuperuser

Utilisez un nom et un mot de passe que vous nÆoublierez pas. Par exemple admin pour le login. En cas dÆoubli, vous pourrez toujours relancer la commande ci-dessus pour crÚer un nouveau superutilisateur avec un nom diffÚrent.

## DÚmarrer le serveur Django

python manage.py runserver

AccÚdez Ó :

* Dashboard:á<http://localhost:8000/>
* Admin:á<http://localhost:8000/admin/>
* Statistiques:á<http://localhost:8000/statistiques/>

VÚrifiez que tout fonctionneá:

![](data:image/png;base64...)

Si vous souhaitez arrÛter le serveur, faire un CTRL+C.

# Concepts ClÚs de Django

## Architecture MVT

Django utilise le patterná**MVT**á(ModÞle-Vue-Template) :

| **Composant** | **R¶le** |
| --- | --- |
| **ModÞle (M)** | Structure des donnÚes (modÞle de base de donnÚes) |
| **Vue (V)** | Logique mÚtier (traitement des requÛtes) |
| **Template (T)** | PrÚsentation HTML (interface utilisateur) |

### Flux de requÛte HTTP :

1. Utilisateur accÞde Ó une URL (ex: /statistiques/)

?

2. Django cherche l'URL dans le fichier **urls.py**

?

3. Django appelle la vue correspondante (view)á: fichier **views.py**

?

4. La vue interroge le modÞle (base de donnÚes)á: fichier **models.py**

?

5. La vue rend le template avec les donnÚesá: fichiers **.html** du dossier **templates**

?

6. Django retourne le HTML au navigateur

## ORM Django

L'ORM (Object Relational Mapper) permet de manipuler la base de donnÚes sans SQL :

# Au lieu de :

# SELECT \* FROM weather\_mesure WHERE temperature > 25

# Vous Úcrivez :

mesures = Mesure.objects.filter(temperature\_\_gt=25)

Aide en ligneá: <https://python.doctor/page-django-query-set-queryset-manager>

## Migrations

Les migrations sont la maniÞre par laquelle Django propage des modifications que vous apportez Ó des modÞles (ajout d'un champ, suppression d'un modÞle, etc.) dans un schÚma de base de donnÚes (fichier models.py) :

python manage.py makemigrations # CrÚer les migrations

python manage.py migrate # Appliquer les migrations

# Configuration de la Base de DonnÚes

Django propose une architecture bien structurÚe : sÚparation entre la logique mÚtier (modÞles), la prÚsentation (templates) et le contr¶le (vues). Cette organisation facilite la maintenance et l'Úvolution de votre code.

Le fichier de configuration ***meteo\_dashboard/settings.py***ácontient les paramÞtres de configuration. VÚrifiez que lÆapplication crÚÚe "meteo" est indiquÚe dans INSTALLED\_APPS ainsi que la configuration pour la langue et le fuseau horaire. Le dossier o¨ seront stockÚs les fichiers statiques (feuilles de style et javascript) doit Ûtre indiquÚ Úgalement :

INSTALLED\_APPS = [

'django.contrib.admin',

'django.contrib.auth',

'django.contrib.contenttypes',

'django.contrib.sessions',

'django.contrib.messages',

'django.contrib.staticfiles',

'meteo',

]

# Base de donnÚes SQLite

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.sqlite3',

'NAME': BASE\_DIR / 'db.sqlite3',

}

}

# Fuseau horaire

TIME\_ZONE = 'Europe/Paris'

USE\_TZ = True

# Langue

LANGUAGE\_CODE = 'fr-fr'

# Configuration des fichiers statiques

STATIC\_URL = '/static/'

STATICFILES\_DIRS = [BASE\_DIR / 'weather' / 'static']

Pour sauvegarder les paramÞtres importants (connexion MQTT et communication sÚcurisÚe avec votre application Django par lÆintermÚdiaire dÆune SECRET-KEY), un fichier fichierá***.env***áest utilisÚ :

MQTT\_BROKER=localhost

MQTT\_PORT=1883

MQTT\_USERNAME=user

MQTT\_PASSWORD=password

DJANGO\_SECRET\_KEY=your-secret-key-here

La clÚ DJANGO\_SECRET\_KEY est une clÚ de sÚcuritÚ secrÞte utilisÚe par Django pour :

1. **Chiffrer les donnÚes sensibles** : Sessions utilisateur, tokens CSRF, mots de passe rÚinitialisÚs, etc.
2. **Signer les donnÚes** : Pour s'assurer que les donnÚes n'ont pas ÚtÚ modifiÚes
3. **GÚnÚrer des tokens de sÚcuritÚ** : Pour les formulaires et les sessions

**Pourquoi c'est important :**

* Si quelqu'un conna¯t votre SECRET\_KEY, il peut forger des sessions, contourner les protections CSRF, et accÚder aux donnÚes chiffrÚes
* Elle **ne doit jamais Ûtre exposÚe** publiquement (GitHub, serveurs, etc.)
* Elle doit Ûtre **unique et alÚatoire**

La DJANGO\_SECRET\_KEY pourra Ûtre gÚnÚrÚe pará:

python -c 'from django.core.management.utils import get\_random\_secret\_key; print(get\_random\_secret\_key())'

1. Chercher Ó quoi sert un token CSRF.
2. CrÚer votre SECRET\_KEY, modifier le fichier .env.

# Publication des tempÚratures

Utiliser MQTTExplorer par exemple pour publier des tempÚratures sur votre broker sur le topic ***meteo/temperature***.

Vous pouvez utiliser ***test.mosquitto.org*** pour faire des tests ou le broker du lycÚe (***172.21.28.1***).

Pour que le site Django place les tempÚratures dans la base de donnÚes, nous allons utilisez un script Python utilisant Paho-MQTT pour souscrire au topic meteo/temperature et inscrire les nouvelles mesures dans la base de donnÚes. Dans un autre terminal, lancer le script ***mqtt\_client.py*** (cf. 12.1) :

python manage.py mqtt\_client

1. Publier plusieurs tempÚratures et observer le fonctionnement du site.
2. Comment rÚagit la page dÆaccueil (dashboard) ?
3. Quelles informations sont affichÚes sur la page statistiques ?
4. Quelles informations sont visibles sur la page dÆadministration ?

![Une image contenant texte, capture dÆÚcran, TracÚ, ligne  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)

# ModÞles de DonnÚes

Pour traduire cette architecture de base de donnÚes en code Django, nous dÚfinissons des modÞles qui reprÚsentent les donnÚes.

Un modÞle est donc une classe python qui hÚrite de la classe ***models.Model***. Les champs sont dÚfinis dans la classe, on leur donne un nom et un type.

![](data:image/png;base64...)

Figure 1 : BDD Ó obtenir

Ouvrir un terminal, aller dans le dossier **/meteo\_config** puis taperá:

python manage.py shell

Importer les modÞlesá:

>>> from meteo.models import \*

Afficher tous les enregistrements de la table Mesureá:

>>> Mesure.objects.all()

1. A quoi sert la classe modÞle ? Que fait la mÚthode all() ?

Filter les mesuresá:

>>> Mesure.objects.filter(valeur\_\_gt=20)

1. Que fait la mÚthode *filter* ? A quoi sert *\_\_gt=20* ?

Aller sur la page dÆadministrationá(relancer le serveur si nÚcessaire) : <http://127.0.0.1:8000/admin>

CrÚez Úventuellement un superuser pour lÆaccÞsá:

python manage.py createsuperuser

Afficher la page des mesuresá: <http://127.0.0.1:8000/admin/weather/mesure/>

Ajouter une mesure infÚrieure Ó 0░C

1. Ecrire la requÛte permettant dÆafficher les valeurs des mesures infÚrieures Ó 0░C. VÚrifier que votre mesure est visible.

>>> quit()

Ouvrirá***meteo/models.py***. Il y a une classe par table de la BDDá:

from django.db import models

class Capteur(models.Model):

"""ModÞle pour les capteurs"""

nom = models.CharField(max\_length=100, unique=True)

type\_capteur = models.CharField(

max\_length=20,

choices=[

('temperature', 'TempÚrature'),

# TODO : Ajouter les choix 'pression' et 'humidite'

]

)

topic\_mqtt = models.CharField(max\_length=100)

date\_creation = models.DateTimeField(auto\_now\_add=True)

def \_\_str\_\_(self):

return f"{self.nom} - {self.get\_type\_capteur\_display()}"

class Meta:

verbose\_name = "Capteur"

verbose\_name\_plural = "Capteurs"

class Mesure(models.Model):

"""ModÞle pour les mesures des capteurs"""

capteur = models.ForeignKey(Capteur, on\_delete=models.CASCADE)

valeur = models.FloatField()

date\_mesure = models.DateTimeField(auto\_now\_add=True)

def \_\_str\_\_(self):

return f"{self.capteur.nom}: {self.valeur}{self.unite}"

class Meta:

verbose\_name = "Mesure"

verbose\_name\_plural = "Mesures"

ordering = ['-date\_mesure']

1. Ajouter le champ ***localisation*** qui contiendra le texte du lieux du capteur (type CharField de 200 caractÞres maxi) dans la table Capteur
2. Ajouter le champ ***actif*** (type boolÚen, vrai par dÚfaut)
3. Dans la table Mesure, ajouter le champ ***unites*** de type texte (longueur max 20 caractÞres) et qui contiendra uniquement le choix possible pour le capteur de tempÚrature : æCÆ pour æ░CÆ.

Si une modification de models.py est faite, il faut appliquez les migrations (cf. 5.3) :

python manage.py makemigrations

python manage.py migrate

# Vues Django

Dans Django, une vue reprÚsente la logique qui traite les requÛtes des utilisateurs et retourne des rÚponses. Ouvrirá***meteo/views.py***áde votre application :

from django.shortcuts import render

from django.http import JsonResponse

from django.views.decorators.http import require\_http\_methods

from django.utils import timezone

from datetime import timedelta

from .models import Capteur, Mesure

import json

def dashboard(request):

"""Affiche le dashboard avec les donnÚes actuelles"""

capteurs = Capteur.objects.all()

# RÚcupÚrer la derniÞre mesure de tempÚrature

mesure\_temp = Mesure.objects.filter(capteur\_\_type\_capteur='temperature').order\_by('date\_mesure').first()

# TODO : RÚcupÚrer les derniÞres mesures de pression et humiditÚ

mesures\_actuelles = {}

if mesure\_temp:

mesures\_actuelles['temperature'] = {

'valeur': mesure\_temp.valeur,

'date': mesure\_temp.date\_mesure,

}

# TODO : Ajouter les mesures de pression et humiditÚ au dictionnaire

context = {

'capteurs': capteurs,

'mesures\_actuelles': mesures\_actuelles,

}

return render(request, 'weather/dashboard.html', context)

def statistiques(request):

"""Affiche les statistiques sur les derniÞres 24 heures"""

depuis = timezone.now() - timedelta(hours=24)

stats = {}

# Statistiques pour la tempÚrature

mesures\_temp = Mesure.objects.filter(

capteur\_\_type\_capteur='temperature',

date\_mesure\_\_gte=depuis

).values\_list('valeur', flat=True)

if mesures\_temp:

stats['temperature'] = {

'min': min(mesures\_temp),

'max': max(mesures\_temp),

'nombre': len(mesures\_temp),

}

# TODO : Ajouter les statistiques pour pression (type\_capteur='pression')

# Utiliser la mÛme structure que pour la tempÚrature

# stats['pression'] = { ... }

# TODO : Ajouter les statistiques pour humiditÚ (type\_capteur='humidite')

# Utiliser la mÛme structure que pour la tempÚrature

# stats['humidite'] = { ... }

context = {

'stats': stats,

}

return render(request, 'weather/statistiques.html', context)

@require\_http\_methods(["GET"])

def mesures\_json(request, type\_capteur):

"""Retourne les mesures au format JSON pour les graphiques"""

# VÚrifier que le type\_capteur est valide

types\_valides = ['temperature'] # TODO : Ajouter 'pression' et 'humidite'

if type\_capteur not in types\_valides:

return JsonResponse({'erreur': 'Type de capteur invalide'}, status=400)

# RÚcupÚrer les mesures des derniÞres 24 heures

depuis = timezone.now() - timedelta(hours=24)

mesures = Mesure.objects.filter(

capteur\_\_type\_capteur=type\_capteur,

date\_mesure\_\_gte=depuis

).order\_by('date\_mesure').values(

'valeur', 'date\_mesure', 'capteur\_\_nom'

)

donnees = [

{

'timestamp': m['date\_mesure'].isoformat(),

'valeur': m['valeur'],

'capteur': m['capteur\_\_nom'],

}

for m in mesures

]

return JsonResponse({'donnees': donnees})

Afficher <http://127.0.0.1:8000/>

Dans la vue ***dashboard*** (***def dashboard(request):*** ci-dessus), il faut afficher les derniÞres mesures.

1. Changer la requÛte pour obtenir la derniÞre mesure.
2. Ajouter la gestion de lÆunitÚ.

Dans la vue ***statistiques***, il faut afficher, en plus des valeurs min et max, la valeur moyenne et le nombre de mesure.

Afficher <http://127.0.0.1:8000/statistiques>

1. Ajouter lÆaffichage de la valeur moyenne.
2. Modifiez la variable capteurs pour prendre en compte que les capteurs actifs.

# Routage (URLs)

Ouvrir le fichier ***meteo/urls.py***á:

from django.urls import path

from . import views

urlpatterns = [

path('', views.dashboard, name='dashboard'),

path('api/mesures/<str:type\_capteur>/', views.mesures\_json, name='mesures\_json'),

path('statistiques/', views.statistiques, name='statistiques'),

]

1. Quelle url utiliser pour afficher les mesures de tempÚrature au formats json ? VÚrifiez.

Ouvrirá***meteo\_dashboard/urls.py***áqui permettra de prendre en compte ce fichier :

from django.contrib import admin

from django.urls import path, include

urlpatterns = [

path('admin/', admin.site.urls),

path('', include('meteo.urls')),

]

1. Quelle ligne permet de dÚfinir la page dÆadministration ?
2. Changer pour accÚder Ó lÆinterface dÆadministration par lÆurl <http://127.0.0.1:8000/administration>

# Templates

Les templates permettent la prÚsentation visuelle de votre siteá:

* fichier qui contient des variables et des tags, et qui sert Ó gÚnÚrer le document final.
* on peut l'utiliser pour gÚnÚrer du html, du csv ou n'importe quel autre fichier basÚ sur du texte.
* les variables sont ÚvaluÚes par {{myVar}}.
* les tags sont Ó un format du type {% myTag ... %}.

## base.html

Ouvrir le fichier ***meteo/templates/meteo/base.html***

{% load static %}

<!DOCTYPE html>

<html lang="fr">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{% block title %}Dashboard MÚtÚo{% endblock %}</title>

<link rel="stylesheet" href="{% static 'meteo/css/style.css' %}">

{% block extra\_css %}{% endblock %}

</head>

<body>

<nav class="navbar">

<div class="container">

<span class="navbar-brand">?? Dashboard MÚtÚo</span>

</div>

</nav>

<div class="container">

{% block content %}{% endblock %}

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>

<script src="{% static 'weather/js/charts.js' %}"></script>

{% block extra\_js %}{% endblock %}

</body>

</html>

La page ***base.html*** sert de base aux pages ***dashboard.html*** et ***statistiques.html***. Les blocs ***extra\_css*** (dÚlimitÚ par le tag {% block extra\_css %}{% endblock %}), ***content*** et ***extra\_js*** sont donc implÚmentÚs dans ***base.html*** mais seront dÚfinis diffÚremment dans les pages dashboard.html et statistiques.html.

1. Changer le texte de la balise ***navbar-brand*** (vous pouvez utiliser <https://www.w3schools.com/charsets/ref_emoji_weather.asp> pour trouver dÆautres icones)

Commenter les lignes {% load static %} et <link rel="stylesheet" href="{% static 'meteo/css/style.css' %}"> (en mettant entre balises <!-- -->)

1. A quoi sert le tag {% load static %} ?
2. Comment est chargÚ la feuille de style ?

Commenter la ligne {% block extra\_css %}{% endblock %}

1. O¨ se trouve la feuille de style concernÚe ?

## dashboard.html

Ouvrirá***meteo/templates/meteo/dashboard.html***á:

{% extends 'meteo/base.html' %}

{% load static %}

{% block title %}Dashboard - MÚtÚo{% endblock %}

{% block extra\_css %}

<link rel="stylesheet" href="{% static 'meteo/css/dashboard.css' %}">

{% endblock %}

{% block content %}

<h1>Dashboard en Temps RÚel</h1>

<!-- MÚtriques actuelles -->

<div class="metrics-grid">

{% if mesures\_actuelles.temperature %}

<div class="metric-card">

<div class="metric-icon">??</div>

<div class="metric-label">TempÚrature</div>

<div class="metric-value">

{{ mesures\_actuelles.temperature.valeur|floatformat:1 }}░C

</div>

<small class="metric-date">

Mise Ó jour: {{ mesures\_actuelles.temperature.date|date:"H:i:s" }}

</small>

</div>

{% endif %}

<!-- TODO : Ajouter les cartes pour pression et humiditÚ ici -->

</div>

<!-- Graphiques -->

<div class="charts-grid">

<div class="chart-container">

<canvas id="temperatureChart"></canvas>

</div>

<!-- TODO : Ajouter les conteneurs graphiques pour pression et humiditÚ -->

</div>

{% endblock %}

1. Que signifie le tag {% if mesures\_actuelles.temperature %}
2. Dans quel fichier cette variable a-t-elle ÚtÚ dÚfinie ?

# Configuration Admin Django

Ouvrirá***meteo/admin.py***á:

from django.contrib import admin

from .models import Capteur, Mesure

@admin.register(Capteur)

class CapteurAdmin(admin.ModelAdmin):

list\_display = ('nom', 'type\_capteur', 'date\_creation')

list\_filter = ('type\_capteur', 'date\_creation')

search\_fields = ('nom',)

readonly\_fields = ('date\_creation',)

@admin.register(Mesure)

class MesureAdmin(admin.ModelAdmin):

list\_display = ('capteur', 'valeur', 'date\_mesure')

list\_filter = ('capteur\_\_type\_capteur', 'date\_mesure')

search\_fields = ('capteur\_\_nom',)

readonly\_fields = ('date\_mesure',)

date\_hierarchy = 'date\_mesure'

1. Modifier admin.py pour prendre en compte lÆaffichage des champs ajoutÚs prÚcÚdemment dans models.py

## DÚmarrer le client MQTT

Afin de lancer le script Python mqtt\_client.py situÚ dans le dossier **meteo** il faut utiliser une commande Django. Ce programme est placÚ dans le dossier ***meteo/management/commands/*** et se nomme ***mqtt\_client.py*** :

from django.core.management.base import BaseCommand

from meteo.mqtt\_client import meteoMQTTClient

class Command(BaseCommand):

help = 'DÚmarre le client MQTT pour collecter la tempÚrature'

def handle(self, \*args, \*\*options):

client = meteoMQTTClient()

client.start()

Pour le lancer, utilisez le nom du fichier :

python manage.py mqtt\_client

# Test avec MQTTExplorer

## Publier des donnÚes de test

![Une image contenant texte, capture dÆÚcran, Police, nombre  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)Vous devez obtenirádans VSCODE : ![](data:image/png;base64...)

# EXERCICES : Ajouter la Pression et l'HumiditÚ

1. Modifiez les fichiers suivants pour ajouter support pour la pression et l'humiditÚ :
   1. ***models.py*** : Ajouter 'pression' et æhumidite' aux choix du type\_capteur et unite
   2. ***views.py*** : Ajouter le traitement pour pression et humiditÚ (remplacer les TODO)
   3. ***urls.py*** : Ajouter les routes si nÚcessaire
   4. ***dashboard.html*** : Ajouter les cartes pour pression et humiditÚ
   5. ***dashboard.css*** : Adapter le CSS si nÚcessaire
   6. ***charts.js*** : Ajouter les appels createChart pour les deux nouveaux graphiques
   7. ***mqtt\_client.py*** : Ajouter les configurations pour les topics MQTT (dÚcommenter la ligne pour prendre en compte lÆunitÚ de la temperature)

Topics MQTT Ó utiliser :

* meteo/pression ? valeur en hPa
* meteo/humidite ? valeur en %
* Et sur votre site Djangoá:
* ![Une image contenant texte, diagramme, capture dÆÚcran, TracÚ  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)![Une image contenant texte, capture dÆÚcran, logiciel, Ic¶ne dÆordinateur  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)
* ![Une image contenant texte, capture dÆÚcran, Police, logiciel  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...) ![Une image contenant texte, capture dÆÚcran, Police, nombre  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)
* ![Une image contenant texte, capture dÆÚcran, nombre  Le contenu gÚnÚrÚ par lÆIA peut Ûtre incorrect.](data:image/png;base64...)

# Comment crÚer un projet Django

## CrÚer le projet

django-admin startproject nom\_du\_projet

cd nom\_du\_projet

## CrÚer l'application

python manage.py startapp nom\_de\_l\_apllication

## Configurer lÆapplication

Modifiez le fichier ***nom\_du\_projet/settings.py*** pour, au minimum, ajouter le nom de lÆapplication (cf. 6) :

INSTALLED\_APPS = [

'django.contrib.admin',

'django.contrib.auth',

'django.contrib.contenttypes',

'django.contrib.sessions',

'django.contrib.messages',

'django.contrib.staticfiles',

**'nom\_de\_l\_application',**

]

## Appliquer la migration

python manage.py migrate

Si le fichier ***nom\_du\_projet/nom\_de\_l\_application/models.py*** est modifiÚ pour utiliser une BDD, il faut en avant :

python manage.py makemigrations

## DÚfinir les vues

CrÚer un fichier ***nom\_du\_projet/nom\_de\_l\_application/urls.py*** pour dÚfinir les routes possibles, par exemple :

from django.urls import path

from . import views

urlpatterns = [

path('', views.racine, name='racine'),

path('api/', views.api\_json, name='api\_json'),

path('autres\_pages/', views.autres, name='autres'),

]

Modifiezá***nom\_du\_projet/urls.py***áqui permettra de prendre en compte ce fichier :

from django.contrib import admin

from django.urls import path**, include**

urlpatterns = [

path('admin/', admin.site.urls),

**path('', include('nom\_de\_l\_application.urls')),**

]

## Super utilisateur

Pensez Ó crÚer un super utilisateur pour la partie admin :

python manage.py createsuperuser

## Lancer le serveur

Pour un accÞs localhost uniquement :

python manage.py runserver

Pour un accÞs sur le rÚseau local (port 8000)á:

python manage.py runserver 192.168.1.1á:8000

Il faut alors ajouter lÆip dans les ALLOWED\_HOSTS du fichier ***nom\_du\_projet/settings.py*** :

ALLOWED\_HOSTS = ['192.168.1.1', 'localhost']
