from django.apps import AppConfig


class SelfOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'self_order'
    verbose_name = 'セルフオーダー'