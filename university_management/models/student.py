from odoo import models, fields, _, api


class Student(models.Model):
    _name = 'uni.student'

    student_id = fields.Char(string='Student ID', required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('Student'))
    name = fields.Char(string='Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string='Gender')
    email = fields.Char(string='Email')
    department = fields.Many2one('uni.department', string='Department', required=True)

    @api.model
    def create(self, vals):
        if vals.get('student_id', _('Student') == _('Student')):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('uni.student.id') or _('Student')
        return super(Student, self).create(vals)
