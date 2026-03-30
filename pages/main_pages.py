import allure

from selenium.webdriver.common.by import By
from pages.base_pages import BasePage


class MainPage(BasePage):
    CARD_LINK = (By.XPATH, "//div[@class='category-cards']/a")
    LOGO_LINK = (By.XPATH, ".//header/a")
    CARD_NAME = lambda name: (By.XPATH, f".//h5[text()='{name}']")

    def get_number_cards(self):
        self.wait_presents_of_element_located(MainPage.CARD_LINK)
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)

    @allure.step("Кликаем по лого")
    def click_on_logo(self):
        self.click(MainPage.LOGO_LINK)

    @allure.step("Название карточек соответсовует ожиданию")
    def is_card_with_name_cards(self, name):
        self.wait_until_button_clickable(MainPage.CARD_NAME(name))
        return self.driver.find_element(*MainPage.CARD_NAME(name)).is_displayed()
