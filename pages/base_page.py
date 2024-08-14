from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def get_rid_off_coockies(self):
        try:
            self.driver.get("https://www.lambdatest.com/selenium-playground/")
            WebDriverWait(self.driver, 20).until(
                ec.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonPreferences"))).click()
            self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonStatistics").click()
            self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonMarketing").click()
            self.driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline").click()
        except Exception:
            pass
