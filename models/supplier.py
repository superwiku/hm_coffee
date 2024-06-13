from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'hmcoffee.supplier'
    _description = 'Supplier'
    name = fields.Char(string='Nama Supplier')
    pic = fields.Char(string='PIC')
    bahan_ids = fields.Many2many(comodel_name='hmcoffee.bahan', string='Nama Bahan')
    
    
    
