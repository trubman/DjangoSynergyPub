from django.db.models import Count

from Homework.models import Profession
from django import template
from django.core.cache import cache


register = template.Library()

@register.simple_tag(name='get_list_professions')
def get_professions():
    return Profession.objects.all()

@register.inclusion_tag('homework/list_professions.html')
def show_categories(arg1='Profession', arg2='list'):
    # professions = Profession.objects.all()
    professions = cache.get('professions')
    if not professions:
        professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
        cache.set('professions', professions, 60)
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}

