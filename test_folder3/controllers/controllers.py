# -*- coding: utf-8 -*-
# from odoo import http


# class TestFolder3(http.Controller):
#     @http.route('/test_folder3/test_folder3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_folder3/test_folder3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_folder3.listing', {
#             'root': '/test_folder3/test_folder3',
#             'objects': http.request.env['test_folder3.test_folder3'].search([]),
#         })

#     @http.route('/test_folder3/test_folder3/objects/<model("test_folder3.test_folder3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_folder3.object', {
#             'object': obj
#         })
