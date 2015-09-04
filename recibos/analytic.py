##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp import models, fields, api, _

class account_analytic_account(models.Model):
    _inherit = ["account.analytic.account"]
    
    product = fields.Many2one('product.template', string='Producto')
    product_owner = fields.Char(string='Propiertario', store=False, compute='_get_product_owner')
    
    @api.one
    @api.depends('product')
    def _get_product_owner(self):
       self.product_owner = self.product.owner.name

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

