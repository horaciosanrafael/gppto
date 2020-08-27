from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Description'

    @api.depends('product_uom_qty', 'price_unit', 'discount')
    def _get_last(self):
        if self.product_uom_qty and self.price_unit and self.discount:
            self.descuentos = self.price_unit * self.product_uom_qty * (self.discount/100)
            self.total_bruto = self.price_unit * self.product_uom_qty

    descuentos = fields.Float(readonly= True, compute='_get_last', store=True)
    total_bruto = fields.Float('Total Bruto', readonly=True, compute='_get_last', store=True)

class ModelName(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_total')
    def _amount_all_gp(self):
        """
        Calculará el total de los descuentos y el importe bruto
        """
        for order in self:
            total_descuentos = total_descuentos = 0.0
            total_sin_descuentos = total_sin_descuentos = 0.0
            for line in order.order_line:
                total_descuentos += line.descuentos
                total_sin_descuentos += line.total_bruto
                """
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                """
            order.update({
                'total_sin_descuentos': total_sin_descuentos,
                'total_descuentos' : total_descuentos,

            })

    total_descuentos = fields.Float('Total Descontado', readonly=True, compute='_amount_all_gp', store=True)
    total_sin_descuentos = fields.Float('Total Bruto', readonly=True, compute='_amount_all_gp', store=True)