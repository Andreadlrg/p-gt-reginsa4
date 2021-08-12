# -*- coding: utf-8 -*-
# Copyright 2017
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    no_factura_purc = fields.Char(
        string='No. Factura',
        size=256,
        help='Numero de factura contable',
    )

    no_serie = fields.Char(
        string='Serie',
        size=256,
        help='No. serie de factura contable',
    )

    tipo_fac = fields.Selection(
        string='Tipo de Factura',
        selection=[
            ('FC', 'FC'),
            ('FCE', 'FCE'),
            ('FPC', 'FPC'),
            ('FE', 'FE'),
            ('ND', 'ND'),
            ('NC', 'NC'),
            ('DA', 'DA'),
            ('FA', 'FA'),
            ('FO', 'FO'),
            ('Escritura Publica', 'Escritura Publica'),
        ],
		default='FC',
        help='Tipo de Documento para libros contables SAT',
    )
