from odoo import models, fields

class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Loại phòng'

    name = fields.Char(required=True)
    code = fields.Char()
