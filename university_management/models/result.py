from odoo import fields, models, api


class Result(models.Model):
    _name = 'uni.result'
    _rec_name = 'student_id'

    student_id = fields.Many2one('uni.student', string='Student ID', required=True)
    student_name = fields.Char(string='Name', related='student_id.name')
    email = fields.Char(string='Email', related='student_id.student_email')
    student_department = fields.Char(string='Department', related='student_id.department_name')
    course = fields.Many2one('uni.course_enrollment', string='Course', required=True)
    semester = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
        ('f', 'F'),
    ], default='a', string='Grade')

    course_enrolled = fields.Many2one('uni.course_enrollment', string='Course Enrolled')

    @api.onchange('student_id')
    def domain_enrollment(self):
        return {
            'domain': {
                'course': [('student_enrollment', '=', self.student_id.id)],
            }
        }
