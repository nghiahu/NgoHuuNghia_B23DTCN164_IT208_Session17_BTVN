from odoo import models, fields

class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Khách hàng'

    name = fields.Char(required=True)
    identity_card = fields.Char()
    phone = fields.Char()

    _sql_constraints = [
        ('identity_unique', 'UNIQUE(identity_card)', 'CMND/CCCD đã tồn tại!')
    ]
