from django.apps import AppConfig

#This file need to install models to settings.py

class AdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads'
