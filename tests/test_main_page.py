import allure
import pytest

import data
from pages.main_pages import MainPage


@allure.feature("Тестирование главной страницы")
class TestMainPage:

    @allure.title("Проверка доступности главной страницы")
    @allure.description("Проверка осуществляется соответствию названию загаловка заданным значением")
    def test_main_page_is_available(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        with allure.step("Проверка названия сайта"):
            assert main_page.get_title() == 'demosite'

    @allure.title("Проверка карточек на странице равно 6")
    @allure.description("На странице должно быть 6 карточек")
    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        with allure.step("Проверка кол-ва карточек"):
            assert main_page.get_number_cards() == 6
    
    @allure.title("При клике на лого открывается стартовая страница")
    @allure.description("При клике должна открывается стартовая страница")
    def test_click_on_logo_go_to_main_page(self, driver):
        """
        открыть страницу заданным url,
        подождали пока загрузится,
        нашли лого,
        кликнуть по logo,
        проверить что title соответвует ожидаемому значению.
        """

        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        main_page.click_on_logo()
        
        with allure.step("title соответствует ожиданию"):
            assert main_page.get_title() == 'demosite'

    @allure.title("Проверка правильности названия карточки с именем {name_card}")
    @allure.description("Название карточек с именем {name_card}")
    @pytest.mark.parametrize("name_card", ['Elements',
                                           'Forms', 
                                           'Alerts, Frame & Windows', 
                                           'Widgets',
                                           'Interactions', 
                                           'Book Store Application'])
    def test_name_first_card_is_element(self, driver, name_card):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Название карточек соответствует ожиданию"):
            assert main_page.is_card_with_name_cards(name_card)
