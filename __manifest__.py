# -*- coding: utf-8 -*-
{
    "name": "Grupo de solo lectura",
    "version": '17.0.1.0',
    "summary": "Grupo de solo lectura ",
    "description": "Este módulo crea un grupo que permite todas las vistas, pero los permisos de escritura se tendran que añadir manualmente.",
    "license": "LGPL-3",
    "category": "Sales",
    "author": "Adrianh De Lucio Chavero",
    "website": "https://www.linkedin.com/in/adrianh-delucio-chavero/",
    "depends": [
        "sale", "crm",
    ],

    "data": [

        "security/sale_readonly_security.xml",


        "security/sale_readonly_menu.xml",
        
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}


