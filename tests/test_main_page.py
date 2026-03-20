from pages.main_pages import MainPage
import data


class TestMainPage:

    def test_main_page_is_aveleble(self,driver):
        driver.get(data.BASE_URL)
        assert driver.title == 'demosite'

    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        assert main_page.get_number_cards() == 6
    