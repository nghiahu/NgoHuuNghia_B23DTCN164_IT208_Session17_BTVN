from odoo import models, fields

class UniversityCourse(models.Model):
    _name = 'university.course'
    _description = 'University Course'

    name = fields.Char(string='Course Name')
    credit = fields.Integer(string='Credit')
