# -*- coding: utf-8 -*-
{
    "name": "Sales Read-Only Access",
    "version": "17.0.1.0.0",
    "summary": "Grupo de solo lectura para todo lo relacionado con Ventas",
    "description": "Este módulo crea un grupo que solo puede leer todos los modelos de ventas (sale.order, sale.order.line, etc).",
    "category": "Sales",
    "author": "Tu Empresa",
    "website": "https://www.tu_empresa.com",
    "depends": ["sale"],
    "data": [
        "security/sale_readonly_security.xml",
        "security/ir.model.access.csv",
        "security/sale_readonly_menu.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
