from odoo import models, fields, api

class Alat(models.Model):
    _inherit = 'product.template'

    stock = fields.Integer(string='Stock')
    