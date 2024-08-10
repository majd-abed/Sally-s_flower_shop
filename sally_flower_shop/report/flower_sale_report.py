# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class FlowerSaleReport(models.Model):
    _inherit = "flower.sale.report"

    order_id = fields.Many2one("sale.order", string="Sales Order", readonly=True)
    so_line = fields.Many2one("sale.order.line", string="Sales Order Item", readonly=True)
    flower_id = fields.Many2one("flower")
    flower_ivoice_id = fields.Many2one("account.move", string="Invoice", readonly=True, help="Invoice created from this flower")
    