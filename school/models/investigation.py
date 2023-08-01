from odoo import models,fields,api


class Investigation(models.Model):
    _name = "school.investigation"
    _description = "school.description"


    name = fields.Char(string="Name")
    age = fields.Integer(atring="Age")
