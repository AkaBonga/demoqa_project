import allure

import data
from pages.main_pages import MainPage


@allure.feature("Тестирование главной страницы")
class TestMainPage:

    @allure.step("Проверка доступности главной страницы")
    @allure.description("Проверка осуществляется соответствию названию загаловка заданным значением")
    def test_main_page_is_aveleble(self,driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        with allure.step("Проверка названия сайта"):
            assert main_page.get_title() == 'demosite'

    @allure.step("Проверка каточек на странице равно 6")
    @allure.description("На странице должно быть 6 карточек")
    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        with allure.step("Проверка кол-ва карточек"):
            assert main_page.get_number_cards() == 6
    