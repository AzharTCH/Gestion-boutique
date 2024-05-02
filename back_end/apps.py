from django.apps import AppConfig



class BackEndConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'back_end'
    # def ready(self):
    #     import back_end.signals

