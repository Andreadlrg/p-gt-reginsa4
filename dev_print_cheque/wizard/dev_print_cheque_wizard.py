# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class dev_print_cheque_wizard(models.TransientModel):
    _name = "dev.print.cheque.wizard"
    
    @api.model
    def _get_check_formate(self):
        company_id = self.env.user.company_id.id
        formate_id = self.env['cheque.setting'].search([('set_default','=',True),('company_id','=',company_id)],limit=1)
        return formate_id.id
    
    invoice_id = fields.Many2one('account.invoice', string='Invoice')
    payment_ids = fields.Many2many('account.payment',string='Payments')
    payment_id = fields.Many2one('account.payment', string='Payment', required="1")
    
    cheque_formate_id = fields.Many2one('cheque.setting', 'Cheque Formate', default=_get_check_formate, required="1")
    text_free = fields.Char('Free Text')
    partner_text = fields.Char('Partner Title')
    cheque_no = fields.Char('Cheque No')
    
    
    
    @api.onchange('payment_id')
    def onchange_payment_id(self):
        if self.payment_id:
            self.cheque_no = self.payment_id.cheque_no
            
    @api.model
    def default_get(self,vals):
        vals = super(dev_print_cheque_wizard,self).default_get(vals)
        invoice_id = self._context.get('active_id')
        invoice_id = self.env['account.invoice'].browse(invoice_id)
        if not invoice_id.payment_ids:
            raise ValidationError(_("No any payment Create for this invoice"))
        vals.update({
            'invoice_id':invoice_id.id,
            'payment_ids':[(6,0, invoice_id.payment_ids.ids)],
        })
        return  vals
    
    @api.multi
    def print_cheque(self):
        self.payment_id.write({
            'cheque_formate_id':self.cheque_formate_id.id,
            'text_free':self.text_free,
            'partner_text':self.partner_text,
            'cheque_no':self.cheque_no or '',
        })
        return self.env.ref('dev_print_cheque.action_report_print_cheque').report_action(self.payment_id)
   
   



    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
