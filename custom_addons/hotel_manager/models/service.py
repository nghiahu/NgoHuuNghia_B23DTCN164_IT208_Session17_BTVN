from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelService(models.Model):
    _name = 'hotel.service'
    _description = 'Dịch vụ khách sạn'

    name = fields.Char(required=True)
    price = fields.Integer()

    _sql_constraints = [
        ('price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0!')
    ]
