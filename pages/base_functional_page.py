import allure

from locators import Locators
from pages.base_page import BasePage


class BaseFunctionalPage(BasePage):

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        self.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    @allure.step("Клик на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.find_element(*Locators.ORDER_FEED_BUTTON).click()

    @allure.step("Клик по первому ингредиенту")
    def click_on_ingredient(self):
        self.find_element(*Locators.FIRST_INGREDIENT_BUTTON).click()

    @allure.step("Клик по кнопке закрытия окна с деталями ингредиента")
    def click_close_button_on_ingredient_details_window(self):
        self.find_element(*Locators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON).click()
        self.wait_for_element_to_disappear(Locators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step("Перетащить элемент в заказ")
    def drag_ingredient_to_order(self):
        source = self.driver.find_element(*Locators.FIRST_INGREDIENT_BUTTON)
        target = self.driver.find_element(*Locators.TOP_INGREDIENT_TARGET)
        self.drag_and_drop(source, target)

    @allure.step("Получить значение каунтера")
    def get_counter_value(self):
        return self.find_element(*Locators.FIRST_INGREDIENT_COUNTER).text

    @allure.step("Клик по 'Оформить заказ'")
    def click_place_order(self):
        self.find_element(*Locators.PLACE_AN_ORDER_BUTTON).click()
        self.wait_for_element_to_be_clickable(Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step("Установка видимости окна с деталями заказа")
    def check_order_details_window_is_open(self):
        return self.find_element(*Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON).is_displayed()
