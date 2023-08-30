
from odoo import models, fields, api


class soa(models.Model):
    _name = 'soa.soa'
    _description = 'soa.soa'


    @api.model
    def format_amount(self, text):
        return text + 'haha'

