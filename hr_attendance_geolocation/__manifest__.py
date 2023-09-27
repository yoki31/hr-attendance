# Copyright 2019 ForgeFlow S.L.
# Copyright 2023 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Hr Attendance Geolocation",
    "summary": """
        With this module the geolocation of the user is tracked at the
        check-in/check-out step""",
    "version": "14.0.2.0.0",
    "license": "AGPL-3",
    "author": "ForgeFlow S.L., Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/hr-attendance",
    "depends": ["hr_attendance"],
    "data": [
        "views/assets.xml",
        "views/hr_attendance_views.xml",
        "data/location_data.xml",
    ],
}
