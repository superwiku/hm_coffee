from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Penjualan(models.Model):
    _name = 'hmcoffee.penjualan'
    _description = 'model.technical.name'
    referensi = fields.Char(string='No. Referensi', 
                            required=True, 
                            readonly=True, 
                            default=lambda self : _('New')
                            )
    
    user_id = fields.Many2one(comodel_name='res.users', string='Kasir', readonly=True, default=lambda self: self.env.user)    
    
    membership = fields.Boolean(string='Apakah member ?')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Nama Member')    
    name = fields.Char(string='Nama')
    tgl_transaksi = fields.Datetime(string='Tanggal Transaksi', default=fields.Datetime.now())
    detailpenjualan_ids = fields.One2many(
                                        comodel_name='hmcoffee.detailpenjualan', 
                                        inverse_name='penjualan_id', 
                                        string='Detail Penjualan')
    
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')
    
    @api.depends('detailpenjualan_ids')
    def _compute_total_harga(self):
        for rec in self:
            a = self.env['hmcoffee.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal')
            rec.total_harga = sum(a)
    
    def unlink(self):
        if self.detailpenjualan_ids:
            a = []
            for detail in self:
                a = self.env['hmcoffee.detailpenjualan'].search([('penjualan_id','=',detail.id)])
            print (a)
            for bahannya in a:
                bahannya.bahan_id.stok += bahannya.quantity
        record = super(Penjualan, self).unlink()
    
    def write(self, vals):
        for rec in self:
            a = self.env['hmcoffee.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            for data in a:
                if data:
                    data.bahan_id.stok += data.quantity
        record = super(Penjualan, self).write(vals)
        for recc in self:
            b = self.env['hmcoffee.detailpenjualan'].search([('penjualan_id','=',recc.id)])
            for databaru in b:
                if databaru in a:
                    databaru.bahan_id.stok -= databaru.quantity
        return record
    @api.model
    def create(self, vals):
        if vals.get('referensi', _("New")) == _("New"):
            membership = vals.get('membership', False)
            if membership == True:
                vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.penjualanmember') or _("New")
            else:
                vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.penjualannonmember') or _("New")
        record = super(Penjualan, self).create(vals)
        return record


class DetailPenjualan(models.Model):
    _name = 'hmcoffee.detailpenjualan'
    _description = 'model.technical.name'
    
    penjualan_id = fields.Many2one(comodel_name='hmcoffee.penjualan', string='Penjualan')
    bahan_id = fields.Many2one(comodel_name='hmcoffee.bahan', string='Barang')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    quantity = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    
    @api.depends('bahan_id')
    def _compute_harga_satuan(self):
        for rec in self:
            rec.harga_satuan = rec.bahan_id.harga_modal
    
    @api.depends('harga_satuan','quantity')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_satuan * rec.quantity
    
    @api.model
    def create(self, vals):
        record = super(DetailPenjualan, self).create(vals)
        if record.quantity:
            self.env['hmcoffee.bahan'].search([('id','=',record.bahan_id.id)]).write({'stok': record.bahan_id.stok - record.quantity})
        return record

    @api.constrains('quantity')
    def _chackQuantity(self):
        for record in self:
            if record.quantity < 1 :
                raise ValidationError(
                    'Masa mau beli {} cuma {} pcs'
                    . format(record.bahan_id.nama_bahan, record.quantity))
            elif(record.quantity > record.bahan_id.stok):
                raise ValidationError(
                    'Stok {} tidak mencukupi, maksimal pembelian {} pcs'
                    .format(record.bahan_id.nama_bahan, record.bahan_id.stok))
                ubah = {'quantity',':','bahan_id.stok'}
                return {'value':ubah}