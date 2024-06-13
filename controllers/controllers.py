# -*- coding: utf-8 -*-
# from odoo import http


# class Hmcoffee(http.Controller):
#     @http.route('/hmcoffee/hmcoffee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hmcoffee/hmcoffee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hmcoffee.listing', {
#             'root': '/hmcoffee/hmcoffee',
#             'objects': http.request.env['hmcoffee.hmcoffee'].search([]),
#         })

#     @http.route('/hmcoffee/hmcoffee/objects/<model("hmcoffee.hmcoffee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hmcoffee.object', {
#             'object': obj
#         })
