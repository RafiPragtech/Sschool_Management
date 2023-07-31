from odoo import fields,models,api

class Student(models.Model):
    _name = "school.student"
    _description = "school.description"


    name = fields.Char(string="Name",required=True)
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age")
    place = fields.Char(string="Place")
    
        