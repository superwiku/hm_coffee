from odoo import models, fields

class Pelanggan(models.Model):
    _name = 'hmcoffee.pelanggan'
    _description = 'Pelanggan'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    
    
