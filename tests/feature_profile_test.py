from base.base_test import BaseTest


class ProfileFeatureTest(BaseTest):

    def test_chenge_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login("")
        self.login_page.enter_password("")
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name("")
        self.personal_page.save_changes()
        self.personal_page.is_change_saved()
