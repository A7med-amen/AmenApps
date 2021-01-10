# -*- coding: utf-8 -*-
# Copyright 2021 Ahmed Amen.
from odoo import models, api,_
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def create_reverse(self,picking):
        picking_obj=self.env['stock.picking']
        return_picking_type_id = picking.picking_type_id.return_picking_type_id
        if return_picking_type_id:
            vals = {
                'picking_type_id': return_picking_type_id.id,
                'origin': picking.name,
                'partner_id': picking.partner_id.id
            }
            picking_id = picking_obj.new(vals)
            picking_id.onchange_picking_type()
            for move_line in picking.move_lines:
                move_id = move_line.new({'product_id': move_line.product_id.id})
                move_id.onchange_product_id()
                move_id.update({
                    'product_uom_qty': move_line.product_uom_qty,
                    'location_id': move_line.location_dest_id.id,
                    'purchase_line_id': move_line.purchase_line_id.id,
                    'location_dest_id': move_line.location_id.id})
                picking_id.move_lines += move_id
                print('move_id >>',move_id)
            vals = picking_id._convert_to_write(picking_id._cache)
            vals['location_id'] = picking.location_dest_id.id
            vals['location_dest_id'] = picking.location_id.id
            vals_move_lines = []
            for vals_move_line in vals['move_lines']:
                if vals_move_line[0] == 0:
                    vals_move_lines.append(vals_move_line)
            vals['move_lines'] = vals_move_lines
            picking_id = picking_obj.create(vals)
            return picking_id

    @api.multi
    def action_cancel_purchase_order(self):
        for pick in self.picking_ids:
            if pick.state !='done':
                pick.action_cancel()
            else:
                rev_pick = self.create_reverse(pick)
                for line in rev_pick.move_lines:
                    line.quantity_done = line.product_uom_qty
                rev_pick.action_assign()
                rev_pick.button_validate()
                rev_pick.action_done()
            if self.invoice_ids:
                for inv in self.invoice_ids:
                    for rec in inv.payment_ids:
                        rec.cancel()
                    inv.action_invoice_cancel()

            self.write({'state': 'cancel'})

