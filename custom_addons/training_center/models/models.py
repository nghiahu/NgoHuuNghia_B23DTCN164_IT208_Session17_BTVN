# -*- coding: utf-8 -*-

from odoo import models, fields, api

# 1. MODEL MÔN HỌC
class TrainingSubject(models.Model):
    _name = 'training.subject'
    _description = 'Môn học'

    name = fields.Char(string="Tên môn", required=True)
    code = fields.Char(string="Mã môn")
    description = fields.Text(string="Mô tả đề cương")

# 2. MODEL GIẢNG VIÊN
class TrainingTeacher(models.Model):
    _name = 'training.teacher'
    _description = 'Giảng viên'

    name = fields.Char(string="Tên giảng viên", required=True)
    phone = fields.Char(string="Số điện thoại")
    skills = fields.Text(string="Kỹ năng")

# 3. MODEL SINH VIÊN
class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Sinh viên'

    name = fields.Char(string="Tên sinh viên", required=True)
    email = fields.Char(string="Email")
    student_id = fields.Char(string="Mã sinh viên")

# 4. MODEL LỚP HỌC
class TrainingClass(models.Model):
    _name = 'training.class'
    _description = 'Lớp học'

    name = fields.Char(string="Tên lớp", required=True)
    start_date = fields.Date(string="Ngày bắt đầu")
    end_date = fields.Date(string="Ngày kết thúc")
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Đang mở'),
        ('closed', 'Đã đóng')
    ], string="Trạng thái", default='draft')
    price_per_student = fields.Integer(string="Học phí/nguời", default=1000000)
    total_revenue = fields.Integer(string="Doanh thu 1 lớp", compute='_compute_revenue')
    
    # Relationships
    subject_id = fields.Many2one('training.subject', string="Môn học", required=True)
    teacher_id = fields.Many2one('training.teacher', string="Giảng viên")
    student_ids = fields.Many2many('training.student', string="Danh sách sinh viên")
    session_ids = fields.One2many('training.session', 'class_id', string="Lịch học chi tiết")

    @api.depends('student_ids', 'price_per_student')
    def _compute_revenue(self):
        for record in self:
            record.total_revenue = len(record.student_ids) * record.price_per_student
# 5. MODEL BUỔI HỌC (SESSION)
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Buổi học'

    name = fields.Char(string="Nội dung buổi học", required=True)
    date = fields.Date(string="Ngày học", default=fields.Date.today)
    duration = fields.Integer(string="Thời lượng (phút)")
    
    # Many2one ngược về Lớp học
    class_id = fields.Many2one('training.class', string="Lớp học")