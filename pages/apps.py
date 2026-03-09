from suit.apps import DjangoSuitConfig
from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
    
class SuitConfig(DjangoSuitConfig):
    # layout = 'horizontal'
    layout = 'vertical'
