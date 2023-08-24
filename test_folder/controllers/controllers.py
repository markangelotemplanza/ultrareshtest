# -*- coding: utf-8 -*-
# from odoo import http


# class TestFolder(http.Controller):
#     @http.route('/test_folder/test_folder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_folder/test_folder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_folder.listing', {
#             'root': '/test_folder/test_folder',
#             'objects': http.request.env['test_folder.test_folder'].search([]),
#         })

#     @http.route('/test_folder/test_folder/objects/<model("test_folder.test_folder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_folder.object', {
#             'object': obj
#         })
