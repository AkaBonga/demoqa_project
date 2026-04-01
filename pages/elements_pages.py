from pages.base_pages import BasePage
from selenium.webdriver.common.by import By


class ElementPage(BasePage):
    ELEMENTS_LINK = (By.XPATH, "//div[@class='element-group']")

    def get_number_cards(self):
        self.wait_presents_of_element_located(ElementPage.ELEMENTS_LINK)
        cards = self.driver.find_elements(*ElementPage.ELEMENTS_LINK)
        return len(cards)