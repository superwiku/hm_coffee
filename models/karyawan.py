from odoo import models, fields, api

class Karyawan(models.Model):
    _inherit = 'hr.employee'

    user_id = fields.Many2one(comodel_name='res.users', string='Kasir', readonly=True, default=lambda self: self.env.user)    
    is_menikah = fields.Boolean(string='Menikah', default=True)
    
