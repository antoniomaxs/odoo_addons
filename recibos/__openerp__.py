# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                                  #
#################################################################

{
    'name' : 'Recibos',
    'version': '1.0',
    'depends': [
        'base', 'mail', 'product', 'crm'
    ],
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'category': 'Inmobiliaria',
    'description': """
Recibos - Gestión Inmobiliaria
================================================================================
La inmobiliaria alquila una vivienda. 
El propietario paga electricidad y agua mensualmente, y pasa los recibos a la inmobiliaria.
La inmobiliaria ha de gestionar el cobro de los mismos con el inquilino y entregar el dinero al propietario.
No debe hacerse como factura ya que la inmobiliaria no vende estos consumibles ni comisiona..
    """,
    'website': '',
    'data': [
        'recibos_view.xml',
        'product_view.xml',
        'analytic_view.xml',
        'crm_lead_view.xml',
        'data/recibos_data.xml',
        'partner_view.xml',
    ],
    'auto_install': False,
    'installable': True,
}
