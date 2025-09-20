# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class BulkPOOrderLock(models.Model):
    _inherit = 'purchase.order'

    def bulk_purchase_order_lock(self):
        """this method used to sales order confirmation in bulk."""
        for purchase in self:
            if purchase.state  in ['purchase'] and not purchase.locked:
                purchase.update({'locked':True})
