from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta,timezone as timez

class Flower(models.Model):
    _name = 'flower'
 
    _description = 'A model that describe a flower'
    
    common_name = fields.Char()
    scientific_name = fields.Char()
    season_start = fields.Date()
    season_end = fields.Date()
    watering_frequency = fields.Integer()
    watering_amount = fields.Float()
    
    def name_get(self):
        return [(flower.id, "{} ({})".format(flower.scientific_name, flower.common_name)) for flower in self]


weather_api_key = 'bf040b4aea31f035480966fbd010d876'