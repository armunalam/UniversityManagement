from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CourseAssignment(models.Model):
    _name = 'uni.course_assignment'
    _sql_constraints = [
        ('unique_course_assign',
         'UNIQUE(course_assign)',
         'This course has already been assigned.')
    ]

    department = fields.Many2one('uni.department', string='Department', required=True)
    faculty = fields.Many2one('uni.faculty', string='Faculty')
    faculty_credit_left = fields.Float(string='Credits Remaining', related='faculty.credit')
    # faculty_credit_remaining = fields.Float(string='Credits Remaining', related='faculty.credit_taken')
    course_assign = fields.Many2one('uni.course', string='Course')
    c_name = fields.Char(string='Course Code', related='course_assign.course_name')
    course_credit = fields.Float(string='Course Credit', related='course_assign.credit')

    @api.onchange('department')
    def domain_assign(self):
        return {
            'domain': {
                'course_assign': [('department', '=', self.department.id)],
                'faculty': [('department', '=', self.department.id)]
            }
        }

    # @api.onchange('faculty')
    # def onchange_faculty(self):
    #     if self.faculty.credit >= self.course_credit:
    #         self.faculty_credit_remaining = self.faculty_credit - self.course_credit
    #     else:
    #         self.faculty_credit_remaining = 0


    @api.constrains('faculty')
    def update_credits(self):
        if self.faculty.credit < self.course_credit:
            raise ValidationError('This faculty cannot take any more courses.')
        else:
            self.faculty.credit -= self.course_credit

