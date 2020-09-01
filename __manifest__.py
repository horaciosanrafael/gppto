# -*- coding: utf-8 -*-
{
    'name': "Modificación del Ppto en G.P.",

    'summary': """
        Modificamos el presupuesto de G.P. a fin de lograr que aparezca el monto total del descuento en la base
        restando el total de lo presupuestado sin impuestos. Dando como resultado el Neto a sobre el cual se podra
        calcular los impuestos. """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
        'views/reporte_ppto.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
