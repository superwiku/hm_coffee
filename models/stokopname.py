from odoo import models, fields, api

class StokOpname(models.Model):
    _name = 'hmcoffee.stokopname'
    _description = 'model.technical.name'
    name = fields.Char(string='Nama Petugas')
    tgl_stokopname = fields.Date(string='Tanggal Stok Opname', default=fields.Date.today())
    detailstokopname_ids = fields.One2many(comodel_name='hmcoffee.detailstokopname', inverse_name='stokopname_id', string='Detail Opname')
    
    @api.model
    def default_get(self, fields):
        res = super(StokOpname, self).default_get(fields)
        bahan_record = self.env['hmcoffee.bahan'].search([])
        detail_vals = []
        for bahan in bahan_record:
            detail_vals.append((0,0,{
                'bahan_id': bahan.id,
                'check': False,
                'catatan': ''
            }))
        res['detailstokopname_ids'] = detail_vals
        return res

class DetailStokOpname(models.Model):
    _name = 'hmcoffee.detailstokopname'
    _description = 'model.technical.name'

    name = fields.Char(compute='_compute_name', string='Name')
    stok = fields.Char(compute='_compute_stok', string='Stok')
    bahan_id = fields.Many2one(comodel_name='hmcoffee.bahan', string='Bahan')
    check = fields.Boolean(string='Sudah di check')
    catatan = fields.Char(string='Catatan')  
    stokopname_id = fields.Many2one(comodel_name='hmcoffee.stokopname', string='Stokopname')
    

    @api.depends('bahan_id')
    def _compute_stok(self):
        for rec in self:
            rec.stok = rec.bahan_id.stok
    
    @api.depends('bahan_id')
    def _compute_name(self):
        for i in self:
            i.name = i.bahan_id.nama_bahan
    

