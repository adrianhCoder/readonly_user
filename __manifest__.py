# -*- coding: utf-8 -*-
{
    "name": "Grupo de solo lectura",
    "version": '17.0.5.0',
    "summary": "Grupo de solo lectura ",
    "description": "Este módulo crea un grupo que permite todas las vistas y todos los modelos , unicamente en modo de solo lectura.",
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


