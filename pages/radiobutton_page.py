from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RadiobuttonDemoPage(BasePage):
    radio_button_demo_location = (By.XPATH, "//a[contains(text(),'Radio Buttons Demo')]")
    first_radio_button_location = (By.XPATH,
                                   "//p[contains(text(),'Click on button to get the selected value.')]" \
                                   "/parent::div//input[@value='Female']")
    second_radio_button_location = ((By.XPATH, "//h4[contains(text(),'Gender')]/following::input[@value='Male']"),
                                    (By.XPATH, "//h4[contains(text(),'Age')]/following::input[@value='5 - 15']"))
    confirmation_location = ((By.ID, "buttoncheck"), (By.XPATH, "//button[text()='Get values']"))
    first_response_location = (By.CLASS_NAME, "radiobutton")
    second_response_location = ((By.CSS_SELECTOR, ".genderbutton"), (By.CSS_SELECTOR, ".groupradiobutton"))

    def __init__(self, driver):
        super().__init__(driver)
        self.get_rid_off_coockies()

    def change_to_radio_button_page(self):
        self.click(self.radio_button_demo_location)

    def use_radio_button(self, selector):
        if selector == "first":
            self.click(self.first_radio_button_location)
            self.click(self.confirmation_location[0])
        elif selector == "second":
            self.click((self.second_radio_button_location[0]))
            self.click((self.second_radio_button_location[1]))
            self.click(self.confirmation_location[1])

    def get_response(self, selector):
        if selector == "first":
            response = self.get_text(self.first_response_location)
        elif selector == "second":
            response = (f"{self.get_text(self.second_response_location[0])} "
                        f"{self.get_text(self.second_response_location[1])}")
        else:
            response = None
        return response
