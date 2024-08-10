from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta,timezone as timez

class FlowerWatering(models.Model):
    _name = 'flower.water'
 
    _description = 'Flower watering log'
    _order = "date"
    
    serial_id = fields.Many2one("stock.lot")
    date = fields.Date()
   