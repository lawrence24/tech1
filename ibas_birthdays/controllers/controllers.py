# -*- coding: utf-8 -*-
# from odoo import http


# class IbasBirthdays(http.Controller):
#     @http.route('/ibas_birthdays/ibas_birthdays/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ibas_birthdays/ibas_birthdays/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ibas_birthdays.listing', {
#             'root': '/ibas_birthdays/ibas_birthdays',
#             'objects': http.request.env['ibas_birthdays.ibas_birthdays'].search([]),
#         })

#     @http.route('/ibas_birthdays/ibas_birthdays/objects/<model("ibas_birthdays.ibas_birthdays"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ibas_birthdays.object', {
#             'object': obj
#         })
