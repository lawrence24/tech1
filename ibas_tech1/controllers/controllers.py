# -*- coding: utf-8 -*-
# from odoo import http


# class IbasTech1(http.Controller):
#     @http.route('/ibas_tech1/ibas_tech1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ibas_tech1/ibas_tech1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ibas_tech1.listing', {
#             'root': '/ibas_tech1/ibas_tech1',
#             'objects': http.request.env['ibas_tech1.ibas_tech1'].search([]),
#         })

#     @http.route('/ibas_tech1/ibas_tech1/objects/<model("ibas_tech1.ibas_tech1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ibas_tech1.object', {
#             'object': obj
#         })
