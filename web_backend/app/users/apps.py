from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = 'users'
    name = 'app.users'
    
    def ready(self) -> None:
        import app.users.signals
