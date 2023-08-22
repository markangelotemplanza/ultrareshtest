# -*- coding: utf-8 -*-
# from odoo import http


# class Soa(http.Controller):
#     @http.route('/soa/soa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soa/soa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('soa.listing', {
#             'root': '/soa/soa',
#             'objects': http.request.env['soa.soa'].search([]),
#         })

#     @http.route('/soa/soa/objects/<model("soa.soa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soa.object', {
#             'object': obj
#         })
