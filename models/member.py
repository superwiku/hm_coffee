from odoo import models, fields, api

class Member(models.Model):
    _name = 'hmcoffee.member'
    _inherit = 'hmcoffee.manusia'

    no_member = fields.Char(string='Nomor Member')
    
