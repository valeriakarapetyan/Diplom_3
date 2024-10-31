import random
import string
import requests
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators

URL = 'https://stellarburgers.nomoreparties.site/'


class Helpers:
    @staticmethod
    def random_email():
        suffix = "@example.com"
        random_string = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return random_string + suffix

    @staticmethod
    def random_password():
        return "".join(random.choices(string.digits, k=6))

    @staticmethod
    def create_user():
        email = Helpers.random_email()
        password = Helpers.random_password()
        name = "Test_name"

        response = requests.post(f"{URL}/api/auth/register", json={"email": email, "password": password, "name": name})
        access_token = response.json()["accessToken"]

        return email, password, name, access_token

    @staticmethod
    def delete_user(email, access_token):
        requests.delete(f"{URL}/auth/user", json={"email": email}, headers={"Authorization": access_token})

    @staticmethod
    def login(driver, email, password):
        driver.get(URL)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_ON_LOGIN_FORM).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_ON_LOGIN_FORM).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.PLACE_AN_ORDER_BUTTON))

    @staticmethod
    def create_an_order(driver):
        source = driver.find_element(*Locators.FIRST_INGREDIENT_BUTTON)
        target = driver.find_element(*Locators.TOP_INGREDIENT_TARGET)
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON))
