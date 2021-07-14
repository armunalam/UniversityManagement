{
    'name': 'University Management',
    'version': '13.0.1.0.0',
    'category': 'Employees',
    'summary': 'A management module for universities',
    'sequence': '1',
    'license': 'AGPL-3',
    'author': 'Armun Alam',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/department.xml',
        'views/faculty.xml',
        'views/student.xml',
        'views/course.xml',
        'views/result.xml',
        'views/course_assignment.xml',
        'views/classroom.xml',
        'data/sequence.xml'
    ],
    'images': [],
    'installable': True,
    'application': True
}
