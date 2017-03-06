from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu_items = [
        {
            'path': '/2017/',
            'icon': 'fa-home',
            'title': 'Homepage',
        }, {
            'path': reverse('about'),
            'title': 'Event',
            'menu': [
                {
                    'path': reverse('about'),
                    'title': 'About'
                }, {
                    'path': reverse('team_list'),
                    'title': 'Team'
                }, {
                    'path': reverse('financial-aid'),
                    'title': 'Financial Aid'
                }, {
                    'path': reverse('about_code'),
                    'title': 'Code of Conduct'
                },
            ]
        }, {
            'path': reverse('proposals'),
            'title': 'Call for Papers',
        }
    ]

    path = context['request'].path

    for root in menu_items:
        if 'menu' not in root:
            continue

        for child in root['menu']:
            if child['path'] == path:
                root['selected'] = child['selected'] = True

    return {
        'menu_items': menu_items
    }
