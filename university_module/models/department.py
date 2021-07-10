from odoo import models, fields


class Department(models.Model):
    _name = 'uni.department'

    dept_id = fields.Char(string='Department ID')
    name = fields.Char(string='Department Name')
