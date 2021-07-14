from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Classroom(models.Model):
    _name = 'uni.classroom'
    _rec_name = 'course'

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

    @api.constrains('time_from')
    def constraint_from(self):
        query_string = '''
            SELECT cl.id
            FROM uni_classroom cl
            WHERE (((cl.time_from <= {} AND cl.time_to >= {})
               OR (cl.time_from < {} AND cl.time_to > {}))
               OR (cl.time_from >= {} AND cl.time_to <= {}))
              AND cl.room_no = '{}'
              AND cl.day = '{}'
              AND cl.create_date != '{}'
              AND cl.write_date != '{}';
        '''.format(self.time_from, self.time_from,
                   self.time_to, self.time_to,
                   self.time_from, self.time_to,
                   self.room_no, self.day,
                   self.create_date, self.write_date)

        self._cr.execute(query_string)

        print(query_string)
        fetch_data = self._cr.fetchone()
        print(fetch_data)
        if fetch_data:
            print('Found')
            raise ValidationError('The time and room overlap with another course.')
        else:
            print('Not found')


