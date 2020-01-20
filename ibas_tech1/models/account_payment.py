# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class AccountPaymentIbas(models.Model):
    
    _inherit = 'account.payment'    
    description = fields.Text(string='Description')