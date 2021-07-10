from odoo import models, fields


class Student(models.Model):
    _name = 'uni.student'

    name = fields.Char(string='Name')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string='Gender')

    email = fields.Char(string='Email')

    department = fields.Many2one('uni.department', string='Department', required=True)
