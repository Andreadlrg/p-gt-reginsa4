# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

{
    'name': 'Dynamic Print Cheque - Check writing',
    'version': '12.0.1.4',
    'sequence':1,
    'category': 'Account',
    'description': """
         App will  configure and print cheque/check Dynamically for any bank with different Cheque format.

Cheque print, check print, check writing, bank check print, check dynamic, bank cheque, cheque dynamic, cheque printing, bank cheque, dynamic print cheque, cheque payment, payment check, 

    """,
    'author': 'DevIntelle Consulting Service Pvt.Ltd', 
    'website': 'http://www.devintellecs.com',
    'summary':'App will  configure and print cheque/check Dynamically for any bank with different Cheque format',
    'images': [],
    'depends': ['account','account_voucher'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/print_cheque_wizard_views.xml',
        'views/report_print_cheque.xml',
        'views/report_menu.xml',
        'views/cheque_setting_view.xml',
        'views/account_vocher_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
