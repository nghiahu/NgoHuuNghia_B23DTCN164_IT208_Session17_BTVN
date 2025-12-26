from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Phiếu đặt phòng'

    code = fields.Char()
    check_in = fields.Date(default=fields.Date.today)
    check_out = fields.Date()
    duration = fields.Integer(compute='_compute_duration', store=True)
    total_amount = fields.Integer(compute='_compute_total', store=True)

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành')
    ], default='draft')

    customer_id = fields.Many2one('hotel.customer', required=True)
    room_id = fields.Many2one('hotel.room', required=True)
    service_ids = fields.Many2many('hotel.service')

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for rec in self:
            if rec.check_in and rec.check_out:
                rec.duration = (rec.check_out - rec.check_in).days
            else:
                rec.duration = 0

    @api.depends('duration', 'room_id.price_per_night', 'service_ids')
    def _compute_total(self):
        for rec in self:
            room_total = rec.duration * (rec.room_id.price_per_night or 0)
            service_total = sum(rec.service_ids.mapped('price'))
            rec.total_amount = room_total + service_total

    @api.onchange('room_id')
    def _onchange_room(self):
        if self.room_id.status == 'maintenance':
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                }
            }

        if self.room_id.status == 'occupied':
            raise ValidationError("Phòng này đang có khách ở!")

    @api.onchange('check_in')
    def _onchange_check_in(self):
        if self.check_in:
            self.check_out = self.check_in + timedelta(days=1)

    @api.constrains('check_in', 'check_out')
    def _check_date(self):
        for rec in self:
            if rec.check_out and rec.check_in and rec.check_out <= rec.check_in:
                raise ValidationError("Ngày trả phòng không hợp lệ!")
