# -*- coding: utf-8 -*-
{
    'name': "gi_website_extend",

    'summary': """
        """,

    'description': """
        It added some 
    """,

    'author': "Arash Homayounfar",
    'website': "https://github.com/gilaneh/gi_website_extend",
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_blog', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_blog_views.xml',
    ],

    'license': 'LGPL-3',

}
