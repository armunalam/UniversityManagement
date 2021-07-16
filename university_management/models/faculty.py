from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import re


class Faculty(models.Model):
    _name = 'uni.faculty'
    _rec_name = 'name'
    _sql_constraints = [
        ('unique_email_faculty',
         'UNIQUE(faculty_email)',
         'The email you entered already exists.')
    ]

    faculty_id = fields.Char(string='Faculty ID', required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('Faculty'))
    name = fields.Char(string='Name')
    faculty_email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    contact_no = fields.Char(string='Contact No.')
    department = fields.Many2one('uni.department', string='Department', required=True)
    credit = fields.Float(string='Credits To Be Taken')
    # credit_taken = fields.Float(string='Credits To Be Taken', default=0)
    designation = fields.Selection([
        ('professor', 'Professor'),
        ('associate_professor', 'Associate Professor'),
        ('assistant_professor', 'Assistant Professor'),
        ('senior_lecturer', 'Senior Lecturer'),
        ('lecturer', 'Lecturer')
    ], default='lecturer', string='Designation')

    @api.model
    def create(self, vals):
        if vals.get('faculty_id', _('Faculty') == _('Faculty')):
            vals['faculty_id'] = self.env['ir.sequence'].next_by_code('uni.faculty.id') or _('Faculty')
        return super(Faculty, self).create(vals)

    @api.constrains('faculty_email')
    def validate_email(self):
        if self.faculty_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                             self.faculty_email)
            if match is None:
                raise ValidationError('Please enter a valid email address.')

    @api.constrains('credit')
    def check_credit_range(self):
        for record in self:
            if record.credit < 0:
                raise ValidationError('The number of credits cannot be a negative value.')
