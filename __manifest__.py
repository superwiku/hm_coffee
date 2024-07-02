# -*- coding: utf-8 -*-
{
    'name': "hmcoffee",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'productivity',
    'application': True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/referensi_penjualan.xml',
        'views/menu.xml', 
        'views/views.xml',
        'views/templates.xml',  
        'wizard/reportpenjualanwz_view.xml',
        'report/report.xml',  
        'report/report_penjualan_template_pdf.xml',     
        'report/report_penjualan_template_wizard_pdf.xml',       
        'views/pegawai_view.xml',
        'views/pelanggan_view.xml',
        'views/kategoribahan_view.xml',
        'views/bahan_view.xml',
        'views/supplier_view.xml',
        'views/pembelian_view.xml',
        'views/penjualan_view.xml',
        'views/karyawan_view.xml',
        'views/stokopname_view.xml',
        'views/alat_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
