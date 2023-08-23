# -*- coding: utf-8 -*-
{
    'name': "soa",
    'author': "Mark",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'reports/soa_report_template.xml',
    ],
    'installable': True,
}
