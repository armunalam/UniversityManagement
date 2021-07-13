from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'uni.course'
    _sql_constraints = [
        ('unique_code_course',
         'UNIQUE(course_code)',
         'The course code must be unique.'),
        ('unique_name_course',
         'UNIQUE(course_name)',
         'The course name must be unique.')
    ]

    course_code = fields.Char(string='Course ID')
    course_name = fields.Char(string='Course Name')
    credit = fields.Float(string='Credit')
    description = fields.Char(string='Description')
    department = fields.Many2one('uni.department', string='Department', required=True)
    semester = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ], default='1', string='Semester')

    @api.constrains('course_code')
    def check_code_length(self):
        for record in self:
            if len(record.course_code) < 5:
                raise ValidationError('The course code must be at least 5 characters long.')

    @api.constrains('credit')
    def check_credit_range(self):
        for record in self:
            if record.credit < 0.5 or record.credit > 5:
                raise ValidationError('The number of credits must be between 0.5 and 5.')

    def name_get(self):
        return [(record.id, record.course_name) for record in self]