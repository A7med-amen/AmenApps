# -*- coding: utf-8 -*-
# Copyright 2021 Ahmed Amen.


{
    "name":"Cancel Purchase Order",
    "summary":"Cancel PO and Bill and Return Picking",
'description': """
    *   This addon help you ( By One Click ) to cancel PO and it's Bill and make picking return 
    """,
    "version":"11.2.0.1",
    "category":"Purchase",
    "author":"Ahmed Amen",
    "license":"AGPL-3",
    "application":False,
    "installable":True,
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 10.0,

    "depends":['purchase','base'],
    "data":[
        "security/purchase_security.xml",
        "views/purchase_view.xml",
    ],
    'images': ['static/description/icon.png'],
    "demo":[
    ],
}
