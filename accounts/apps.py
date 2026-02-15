from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    def ready(self):
        # import signals to ensure they are registered
        try:
            import accounts.signals  # noqa: F401
        except Exception:
            pass
