from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RadiobuttonDemoPage(BasePage):
    radio_button_demo_location = (By.XPATH, "//a[contains(text(),'Radio Buttons Demo')]")
    first_radio_button_location = (By.XPATH,
                                   "//p[contains(text(),'Click on button to get the selected value.')]" \
                                   "/parent::div//input[@value='Female']")
    first_confirmation_location = (By.ID, "buttoncheck")
    firs_response_location = (By.CLASS_NAME, "radiobutton")

    def __init__(self, driver):
        super().__init__(driver)
        self.get_rid_off_coockies()

    def change_to_radio_button_page(self):
        self.click(self.radio_button_demo_location)

    def use_first_radio_button(self):
        self.click(self.first_radio_button_location)
        self.click(self.first_confirmation_location)

    def get_first_response(self):
        first_response = self.get_text(self.firs_response_location)
        return first_response
