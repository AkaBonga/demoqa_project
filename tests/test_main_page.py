def test_main_page_is_evalable(driver):
    driver.get('https://demoqa.com/')
    assert driver.title=='demosite'
