from odoo import models, fields


class Course(models.Model):
    _name = 'uni.course'

    course_id = fields.Char(string="Course ID")
    name = fields.Char(string="Course Name")
    department = fields.Many2one('uni.department', string='Department', required=True)
    faculty = fields.Many2one('uni.faculty', string='Faculty', required=True)
    student_course = fields.One2many('uni.course.many', 'student_course_id', string='Students')


class CourseMany(models.Model):
    _name = 'uni.course.many'

    student_id = fields.Many2one('uni.student', string='Student Name')
    student_email = fields.Char(string='Email', related='student_id.email')
    student_course_id = fields.Many2one('uni.course', string='Course ID')
