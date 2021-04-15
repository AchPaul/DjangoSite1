from django import template

from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')#Пользов. тег категорий для гл. страницы
def get_categories():
    return Category.objects.order_by('name')


