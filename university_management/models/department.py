from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Department(models.Model):
    _name = 'uni.department'
    _rec_name = 'dept_name'
    _sql_constraints = [
        ('unique_code_department',
         'UNIQUE(dept_code)',
         'The department code must be unique.'),
        ('unique_dept_name_department',
         'UNIQUE(dept_name)',
         'The department name must be unique.')
    ]

    dept_code = fields.Char(string='Code')
    dept_name = fields.Char(string='Name')

    @api.constrains('dept_code')
    def check_code_length(self):
        for record in self:
            if len(record.dept_code) < 2 or len(record.dept_code) > 7:
                raise ValidationError('The department code must be between 2 and 7 characters long.')

    # def name_get(self):
    #     return [(record.id, record.dept_name) for record in self]
