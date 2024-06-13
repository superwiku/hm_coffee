from odoo import models, fields, api

class Pembelian(models.Model):
    _name = 'hmcoffee.pembelian'
    _description = 'Pembelian'

    name = fields.Char(string='No Referensi')    
    supplier_id = fields.Many2one(comodel_name='hmcoffee.supplier', string='Nama Supplier')
    tgl_pembelian = fields.Datetime(string='Tanggal Pembelian' , default=fields.Datetime.now())  
    detailpembelian_ids = fields.One2many(
        comodel_name='hmcoffee.detailpembelian', 
        inverse_name='pembelian_id', 
        string='Detail Pembelian')
    total_pembelian = fields.Integer(compute='_compute_total_pembelian', string='Total Pembelian', default = 0)
    
    @api.depends('detailpembelian_ids')
    def _compute_total_pembelian(self):
        for rec in self:
            a = self.env['hmcoffee.detailpembelian'].search([('pembelian_id','=',rec.id)]).mapped('subtotal')
            rec.total_pembelian = sum(a)

    
    def unlink(self):
        if self.detailpembelian_ids:
            a = []
            for detail in self:
                a = self.env['hmcoffee.detailpembelian'].search([('pembelian_id','=',detail.id)])
            print (a)
            for bahannya in a:
                bahannya.bahan_id.stok -= bahannya.qty
        record = super(Pembelian, self).unlink()
    
    def write(self, vals):
        for rec in self:
            a = self.env['hmcoffee.detailpembelian'].search([('pembelian_id','=',rec.id)])
            for data in a:
                if data:
                    data.bahan_id.stok -= data.qty
        record = super(Pembelian, self).write(vals)
        for recc in self:
            b = self.env['hmcoffee.detailpembelian'].search([('pembelian_id','=',recc.id)])
            for databaru in b:
                if databaru in a:
                    databaru.bahan_id.stok += databaru.qty
        return record

class DetailPembelian(models.Model):
    _name =  'hmcoffee.detailpembelian'
    _description =  'DetailPembelian'

    pembelian_id = fields.Many2one(comodel_name='hmcoffee.pembelian', string='Pembelian')
    bahan_id = fields.Many2one(comodel_name='hmcoffee.bahan', string='Item Pembelian')
    modal = fields.Integer(string='Harga Modal')
    harga_modal = fields.Integer(string='Modal')    
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
            
    @api.onchange('bahan_id')
    def _onchange_bahan(self):
        self.harga_modal = self.bahan_id.harga_modal

    @api.depends('modal','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_modal * rec.qty
    
    @api.model
    def create(self, vals):
        record = super(DetailPembelian, self).create(vals)
        if record.qty:
            self.env['hmcoffee.bahan'].search([('id','=',record.bahan_id.id)]).write({'stok': record.bahan_id.stok + record.qty})
        return record