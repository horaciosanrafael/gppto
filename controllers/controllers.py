# -*- coding: utf-8 -*-
# from odoo import http


# class /home/horacio/odoo1303/misapps/gpppto(http.Controller):
#     @http.route('//home/horacio/odoo1303/misapps/gpppto//home/horacio/odoo1303/misapps/gpppto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/horacio/odoo1303/misapps/gpppto//home/horacio/odoo1303/misapps/gpppto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/horacio/odoo1303/misapps/gpppto.listing', {
#             'root': '//home/horacio/odoo1303/misapps/gpppto//home/horacio/odoo1303/misapps/gpppto',
#             'objects': http.request.env['/home/horacio/odoo1303/misapps/gpppto./home/horacio/odoo1303/misapps/gpppto'].search([]),
#         })

#     @http.route('//home/horacio/odoo1303/misapps/gpppto//home/horacio/odoo1303/misapps/gpppto/objects/<model("/home/horacio/odoo1303/misapps/gpppto./home/horacio/odoo1303/misapps/gpppto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/horacio/odoo1303/misapps/gpppto.object', {
#             'object': obj
#         })
