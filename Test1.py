import time
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def testing():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()


def test_show_my_pets(testing):
    testing.find_element(By.ID, 'email').send_keys('lbtumatym1@gmail.com')
    testing.find_element(By.ID, 'pass').send_keys('77777')
    time.sleep(2)
    # замените все на ваши данные или данные из settings.
    # далее по аналогии с материалами курса