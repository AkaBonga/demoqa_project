import pytest
import chromedriver_autoinstaller
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def setup_chromedriver():
    """Автоматически устанавливает chromedriver, если он не найден в PATH."""
    chromedriver_autoinstaller.install()

@pytest.fixture
def driver():
    """Фикстура, создающая экземпляр браузера Chrome."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()