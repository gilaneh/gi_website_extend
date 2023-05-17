# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GiWebsiteBlog(models.Model):
    _inherit = 'blog.blog'

    editors = fields.Many2many('res.users')

