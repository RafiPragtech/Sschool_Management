from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "school.description"


    name = fields.Char(string="Name",required=True)
    subject = fields.Selection([
        ('maths',"Maths"),
        ('malayalam','Malayalam'),
        ('english','English'),
        ('biology','Biology'),
        ('chemistry','Chemistry'),
        ('physics','Physics')
    ])
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(compute="_compute", string="Age")
    place = fields.Char(string="Place")

          
    @api.depends('dob')
    def _compute(self):
        for record in self:
            delta = relativedelta(date.today(),record.dob)
            print("...........delta.......",delta)
            record.age = delta.years
    
        
    
