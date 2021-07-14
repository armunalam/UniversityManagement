from odoo import fields, models, api


class Classroom(models.Model):
    _name = 'uni.classroom'

    department = fields.Many2one('uni.department', string='Department', required=True)
    course = fields.Many2one('uni.course', string='Course', required=True)
    room_no = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9')
    ], default='0', string='Room No.')
    day = fields.Selection([
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday')
    ], default='sunday', string='Room No.')
    time_from = fields.Float(string='From')
    time_to = fields.Float(string='To')

    @api.onchange('department')
    def domain_assign(self):
        return {
            'domain': {
                'course': [('department', '=', self.department.id)],
            }
        }