import allure
import data

from elements_pages import ElementPage


class TestElements:

    def test_element_page_is_available(self, driver):
        main_page = ElementPage(driver)
        main_page.open(data.ELEMENTS_URL)
        
        with allure.step("Проверка названия сайта"):
            assert main_page.get_title() == 'demosite'

    def test_number_of_elements_is_six(self, driver):
        main_page = ElementPage(driver)
        main_page.open(data.ELEMENTS_URL)
        
        with allure.step("Проверка кол-ва элементов на странице"):
            assert main_page.get_number_cards() == 6