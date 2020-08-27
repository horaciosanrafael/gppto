# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/horacio/odoo1303/misapps/gpppto(models.Model):
#     _name = '/home/horacio/odoo1303/misapps/gpppto./home/horacio/odoo1303/misapps/gpppto'
#     _description = '/home/horacio/odoo1303/misapps/gpppto./home/horacio/odoo1303/misapps/gpppto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
