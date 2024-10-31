import allure
import pytest
from selenium import webdriver

from helpers import URL, Helpers
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from pages.pass_recovery_page import PassRecoveryPage
from pages.base_functional_page import BaseFunctionalPage


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser = request.param
    allure.dynamic.title(f"Тестирование в {browser}")
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver_instance = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        driver_instance = webdriver.Chrome(options=options)

    driver_instance.get(URL)
    driver_instance.maximize_window()

    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def pass_recovery_page(driver):
    return PassRecoveryPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def base_functional_page(driver):
    return BaseFunctionalPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def create_user():
    email, password, name, access_token = Helpers.create_user()

    yield email, password, name, access_token

    Helpers.delete_user(email, access_token)


@pytest.fixture
def login(driver, create_user):
    creds = create_user
    Helpers.login(driver, creds[0], creds[1])


@pytest.fixture
def create_an_order(driver, login):
    Helpers.create_an_order(driver)
