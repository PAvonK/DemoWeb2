from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #imports all signals
        import users.signals
