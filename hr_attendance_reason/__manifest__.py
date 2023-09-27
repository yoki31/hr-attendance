# Copyright 2017 Odoo S.A.
# Copyright 2018 ForgeFlow, S.L.
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    "name": "HR Attendance Reason",
    "version": "14.0.1.1.3",
    "category": "Human Resources",
    "website": "https://github.com/OCA/hr-attendance",
    "author": "Odoo S.A., Tecnativa, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["hr_attendance"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/assets.xml",
        "views/hr_attendance_reason_view.xml",
        "views/hr_attendance_view.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [
        "demo/hr_attendance_reason_demo.xml",
    ],
    "qweb": ["static/src/xml/attendance.xml"],
}
