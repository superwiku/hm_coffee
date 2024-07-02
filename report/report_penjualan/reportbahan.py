from odoo import models

class BahanXlsx(models.AbstractModel):
    _name = 'report.hmcoffee.report_bahan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, bahan):
        sheet = workbook.add_worksheet('Daftar Bahan')
        row = 1
        col = 0
        sheet.write(row,col,'Nama Bahan')
        sheet.write(row+1,col,'Kondisi Stok')
        for obj in bahan:
            row = 1
            col +=1
            sheet.write(row,col,obj.nama_bahan)
            sheet.write(row+1,col,obj.kondisi_stok)