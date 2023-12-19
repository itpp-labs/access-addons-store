from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestUi(HttpCase):
    def test_01_check_logo(self):
        self.start_tour(
            "/web",
            "pos_debranding.tour",
            login="admin",
            timeout=240,
        )
