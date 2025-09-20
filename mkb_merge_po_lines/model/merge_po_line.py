# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class MergeDuplicatePoLines(models.Model):
    _inherit = 'purchase.order'

    def merge_duplicate_po_lines(self):
        for purchase in self:
            purchase_lines = {}
            for line in purchase.order_line:
                key = (line.product_id.id, line.price_unit, tuple(sorted((tax.id for tax in line.tax_ids))))
                if key in purchase_lines:
                    purchase_lines[key].product_qty += line.product_qty
                    line.unlink()
                else:
                    purchase_lines[key] = line
        return True
