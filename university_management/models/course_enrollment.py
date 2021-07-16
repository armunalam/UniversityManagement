from odoo import fields, models, api


class CourseEnrollment(models.Model):
    _name = 'uni.course_enrollment'
    _rec_name = 'course_enrollment'
    _sql_constraints = [
        ('unique_student_enrollment',
         'UNIQUE(student_enrollment, course_enrollment)',
         'This student has already enrolled for this course.')
    ]

    student_enrollment = fields.Many2one('uni.student', string='Student ID', required=True)
    name = fields.Char(string='Name', related='student_enrollment.name')
    email = fields.Char(string='Email', related='student_enrollment.student_email')
    department = fields.Char(string='Department', related='student_enrollment.department_name')

    course_enrollment = fields.Many2one('uni.course', string='Course', required=True)
    date = fields.Date(string='Date', default=fields.Date.context_today)

    @api.onchange('department')
    def domain_enrollment(self):
        return {
            'domain': {
                'course_enrollment': [('department', '=', self.department)],
            }
        }
