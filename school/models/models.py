from odoo import models, fields, api


class School(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    classe = fields.Selection([
        ('cls_a','10 A'),
        ('cls_b','!0 B'),
        ('cls_c','10 C'),
        ('cls_d','10 D'),
    ])
