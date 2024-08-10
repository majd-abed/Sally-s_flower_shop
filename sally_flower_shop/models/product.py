from datetime import datetime
from odoo import fields, models, api

class Product(models.Model):

    _inherit = "product.product"

    is_flower = fields.Boolean("Is Flower")
    flower_id = fields.Many2one("flower")
    sequence_id = fields.Many2one("ir.sequence", "Flower Sequence")
    gardener_ids = fields.Many2many("res.users", string = "Gardeners")


    
    def action_needs_watering(self):
        flowers = self.env["product.product"].search([("is_flower", "=", True)])
        serials = self.env["stock.lot"].search([("product_id", "in", flowers.ids)])
        lot_vals = defaultdict(bool)
        for serial in serials:
            if serial.water_ids:
                last_watered_date = serial.water_ids[0].date
                frequency = serial.product_id.flower_id.watering_frequency
                today = fields.Date.today()
                needs_watering = (today - last_watered_date).days >= frequency
                lot_vals[serial.product_id.id] |= needs_watering
            else:
                lot_vals[serial.product_id.id] = True
        for flower in flowers:
            flower.needs_watering = lot_vals[flower.id]
        


