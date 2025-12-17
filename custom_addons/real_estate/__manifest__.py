{
    'name': 'Real estate management',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Estate',
    'author': 'Nghia',
    'description': """
This is a module for managing real estate data
    - User
    - Real estate
    - ...
""",
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
