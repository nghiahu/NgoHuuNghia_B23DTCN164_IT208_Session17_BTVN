from odoo import models, fields

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Phòng khách sạn'

    name = fields.Char(required=True)
    floor = fields.Integer()
    price_per_night = fields.Integer()
    status = fields.Selection([
        ('available', 'Trống'),
        ('occupied', 'Đang ở'),
        ('maintenance', 'Bảo trì')
    ], default='available')

    type_id = fields.Many2one('hotel.room.type')

    _sql_constraints = [
        ('room_unique', 'UNIQUE(name)', 'Số phòng đã tồn tại!'),
        ('price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0!')
    ]
