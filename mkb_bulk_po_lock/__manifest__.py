# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Bulk Lock Purchase Orders',
    'version': '1.0.0',
    'summary': 'This app allows you to Lock multiple Purchase order in bulk',
    'description': 'This app allows you to Lock multiple Purchase order in bulk',
    'category': 'Purchase',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'views/purchase_order.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['purchase'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
