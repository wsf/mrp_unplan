from datetime import date
from datetime import datetime, timedelta
from odoo import models, fields, api

class MrpProduction(models.Model):

    _inherit = "mrp.production"
    
    def button_unplan(self):

        self.workorder_ids.leave_id.unlink()
        self.workorder_ids.write({
            'date_start': False,
            'date_finished': False,
        })
