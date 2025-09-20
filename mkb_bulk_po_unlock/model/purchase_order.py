# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class BulkPOOrderUnlock(models.Model):
    _inherit = 'purchase.order'

    def bulk_purchase_order_unlock(self):
        for purchase in self:
            if purchase.state  in ['purchase'] and not purchase.locked:
                purchase.update({'locked':False})
