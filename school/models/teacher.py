
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import fields,models,api

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "school.description"


    name = fields.Char(string="Name",required=True)
    subject = fields.Selection([
        ('malayalam','Malayalam'),
        ('english','english'),
        ('maths','Maths'),
        ('biology','Biology'),
        ('chemistry','Chemistry'),
        ('physics','Physics'),
    ],string="Subject Taken")
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(compute="_compute", string="Age")
    place = fields.Char(string="Place")


    @api.depends('dob')
    def _compute(self):
        for record in self:
            delta = relativedelta(date.today(),record.dob)
            print("...........delta.......",delta)

            record.age = delta.years

