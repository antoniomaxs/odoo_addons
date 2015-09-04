# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                                  #
#################################################################

{
    'name' : 'Evitar notificaciones Calendario',
    'version': '1.0',
    'depends': [
        'base'
    ],
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'category': 'Calendario',
    'description': """
Evitar notificaciones del calendario. Establece la variable de sistema calendar.block_mail a True
    """,
    'website': '',
    'data': [
        'calendar_unnotify_data.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True
}
