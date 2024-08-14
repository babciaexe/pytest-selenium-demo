from tests.base_test import BaseTest
from pages.radiobutton_page import RadiobuttonDemoPage


class TestChangePassword(BaseTest):
    def test_radiobutton_demo_value_1(self):
        radio_button_page = RadiobuttonDemoPage(self.driver)
        radio_button_page.change_to_radio_button_page()
        radio_button_page.use_first_radio_button()
        first_response = radio_button_page.get_first_response()
        assert first_response == "Radio button 'Female' is checked"
