import pytest
from tests.base_test import BaseTest
from pages.radiobutton_page import RadiobuttonDemoPage


class TestChangePassword(BaseTest):
    @pytest.mark.parametrize("selector, expected_response",
                             [("first", "Radio button 'Female' is checked"),
                              ("second", "Male 5 - 15")])
    def test_radiobutton_demo_value_1(self, selector, expected_response):
        radio_button_page = RadiobuttonDemoPage(self.driver)
        radio_button_page.change_to_radio_button_page()
        radio_button_page.use_radio_button(selector)
        response = radio_button_page.get_response(selector)
        if response is None:
            print("Wrong choice argument")
        assert response == expected_response
