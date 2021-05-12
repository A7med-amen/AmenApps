# -*- coding: utf-8 -*-
# Copyright 2021 Ahmed Amen.


{
    "name":"Cancel Confirmed PO / BILL",
    "summary":"Cancel Confirmed PO and Bill and Return Picking",
'description': """
    *   This addon help you ( By One Click ). \n
     1- Cancel Confirmed PO. \n 
     2- Cancel Validated Or paid Vendor Bill. \n 
     3- Make picking return. \n 
    """,
    "version":"11.2.0.1",
    "category":"Purchase",
    "author":"Ahmed Amen",
    'license': 'LGPL-3',
    "application":False,
    "installable":True,
    "depends":['purchase','base'],
    "data":[
        "security/purchase_security.xml",
        "views/purchase_view.xml",
    ],
    'images': ['static/description/logo.png'],
    "demo":[
    ],
}
