import random

from base.base_test import BaseTest


class ProfileFeatureTest(BaseTest):

    def test_chenge_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_change_saved()
