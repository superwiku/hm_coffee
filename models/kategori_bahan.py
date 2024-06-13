from odoo import models, fields, api

class KategoriBahan(models.Model):
    _name = 'hmcoffee.kategoribahan'
    _description = 'KategoriBahan'

    name = fields.Selection(string='Nama Kategori', selection=[('kategori kopi', 'Kopi'), 
                                         ('kategori makanan', 'Makanan'), 
                                         ('kategori minuman', 'Minuman'),], 
                              required=True)
    no_rak = fields.Integer(string='Nomor Rak')
    bahan_ids = fields.One2many(comodel_name='hmcoffee.bahan', 
                                inverse_name='kategori_bahan_id', 
                                string='Daftar Bahan')
    
    
    
