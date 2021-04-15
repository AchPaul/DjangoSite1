from django.db.models import Count
from women.models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Купить подписку', 'url_name': 'buyprog'},
        {'title': 'Обратная связь', 'url_name': 'feedback'},
        {'title': 'Создать статью', 'url_name': 'addpage'},
        ]


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))
        context['cats'] = cats
        context['menu'] = menu
        return context
