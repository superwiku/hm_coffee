from odoo import models, fields, api
class Manusia(models.Model):
    _name = 'hmcoffee.manusia'
    _description = 'Manusia'

    name = fields.Char(string='Nama')
    usia = fields.Integer(string='Usia')
    alamat = fields.Char(string='Alamat')
    
    
    
