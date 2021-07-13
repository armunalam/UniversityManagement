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
        'views/faculty.xml',
        'views/student.xml',
        'views/department.xml',
        'views/course.xml',
        'data/sequence.xml'
    ],
    'images': [],
    'installable': True,
    'application': True
}
