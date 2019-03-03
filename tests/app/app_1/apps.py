from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app_1'

    config_model_name = 'RenamedConfig'
    depends_upon_config = (
        'key_1',
    )
