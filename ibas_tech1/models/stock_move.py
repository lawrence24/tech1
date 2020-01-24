
# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    desc_note = fields.Text(string='Note or Description')

    @api.onchange('desc_note')
    def _onchange_desc_note(self):
        for rec in self:
            rec.move_id.desc_note = rec.desc_note

class StockMove(models.Model):
    _inherit = 'stock.move'
    desc_note = fields.Text(string='Note or Description')
