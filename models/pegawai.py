from odoo import api, models, fields

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
    status = fields.Char(string='status')
    
    @api.onchange('usia')
    def _tentukan_status(self):        
            if self.usia > 30:
                self.status = "tua"
            else:
                self.status = "muda"
    
    
    
    
    
