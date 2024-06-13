from odoo import models, fields, api

class Bahan(models.Model):
    _name = 'hmcoffee.bahan'
    _description = 'Bahan'
    _rec_name = 'nama_bahan'

    nama_bahan = fields.Char(string='Nama Bahan')
    kategori_bahan_id = fields.Many2one(comodel_name='hmcoffee.kategoribahan', string='Kategori')
    stok = fields.Integer(string='Jumlah Stok')
    kondisi_stok = fields.Char(compute='_compute_kondisi_stok', string='kondisi_stok')
    harga_modal = fields.Integer(string='Harga Modal')
    total_modal = fields.Integer(compute='_compute_total_modal', string='Total Modal')
    supplier_ids = fields.Many2many(comodel_name='hmcoffee.supplier', string='Supplier')
    

    @api.depends('stok')
    def _compute_kondisi_stok(self):
        for rec in self:
            if rec.stok < 10:
                rec.kondisi_stok = 'kurang'
            else:
                rec.kondisi_stok = 'cukup'

    @api.depends('stok','harga_modal')
    def _compute_total_modal(self):
        for record in self:
            record.total_modal = record.stok * record.harga_modal
    
    
    
    
