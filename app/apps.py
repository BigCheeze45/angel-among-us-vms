from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    def ready(self):
        # import signal files so we can pick up on django signals
        # & in this case assign initial group permissions
        import app.signals
