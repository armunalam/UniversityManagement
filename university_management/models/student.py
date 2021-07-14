from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import re
from datetime import date


class Student(models.Model):
    _name = 'uni.student'
    _rec_name = 'student_id'
    _sql_constraints = [
        ('unique_email_student',
         'UNIQUE(student_email)',
         'The email you entered already exists.')
    ]

    student_id = fields.Char(string='Student ID', required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('Student'))
    name = fields.Char(string='Name')
    student_email = fields.Char(string='Email')
    contact_no = fields.Char(string='Contact No.')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    address = fields.Text(string='Address')
    department = fields.Many2one('uni.department', string='Department', required=True)
    department_name = fields.Char(string='Department Code', related='department.dept_name')

    @api.model
    def create(self, vals):
        if vals.get('student_id', _('Student') == _('Student')):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('uni.student.id') or _('Student')
        return super(Student, self).create(vals)

    @api.constrains('student_email')
    def validate_email(self):
        if self.student_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                             self.student_email)
            if match is None:
                raise ValidationError('Please enter a valid email address.')

        self.student_id = f'{self.department.dept_code}-{date.today().year}-{self.student_id}'
