from odoo import models, fields

class Pegawai(models.Model):
    _name = 'hmcoffee.pegawai'
    _description = 'model.technical.name'

    name = fields.Char(string='Nama')
    usia = fields.Integer(string='Usia')
    jabatan = fields.Selection(string='Bagian', 
                              selection=[('kasir', 'Kasir'), 
                                         ('akunting', 'Akunting'), 
                                         ('kebersihan', 'Kebersihan'),], 
                              required=True)
    foto = fields.Binary(string='Foto', help='choose picture')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir', default=fields.Datetime.now())
    
    
    
    
    
    
