import allure

from locators import Locators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Клик по 'Лента заказов'")
    def click_order_feed_button(self):
        self.find_element(*Locators.ORDER_FEED_BUTTON).click()
        self.wait_for_element_to_be_clickable(Locators.FIRST_ORDER_AREA)

    @allure.step("Клик по первому заказу в ленте")
    def click_on_first_order_in_feed(self):
        self.find_element(*Locators.FIRST_ORDER_AREA).click()
        self.wait_for_element_to_be_visible(Locators.TOTAL_PRICE_OF_ORDER)

    @allure.step("Установка видимости окна с деталями заказа в ленте")
    def check_order_details_window_in_feed_is_open(self):
        return self.find_element(*Locators.TOTAL_PRICE_OF_ORDER).is_displayed()

    @allure.step("Получение номера заказа после оформления")
    def get_order_ident(self):
        self.wait_for_element_to_disappear(Locators.LOADER)
        return self.find_element(*Locators.ORDER_IDENT).text

    @allure.step("Закрыть окно информации о заказе")
    def close_order_info_window(self):
        self.wait_for_element_to_disappear(Locators.LOADER)
        self.wait_for_element_to_be_clickable(Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON)
        button = self.find_element(*Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON)
        # Пришлось использовать JS, так как обычный клик не проходил даже после ожидания wait_for_element_to_be_clickable
        self.click_by_js(button)
        self.wait_for_element_to_disappear(Locators.ORDER_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step("Найти заказ в разделе 'В работе'")
    def find_order_in_progress(self, ident):
        xpath = self.create_xpath_by_text_in_history(ident)
        self.wait_for_element_to_be_visible_by_xpath(xpath)
        element = self.find_element_by_xpath(xpath)
        return element.is_displayed()

    @allure.step("Получить количество заказов за все время")
    def get_counter_done_by_all_time(self):
        self.click_order_feed_button()
        return self.find_element(*Locators.DONE_BY_ALL_TIME_COUNTER).text

    @allure.step("Получить количество заказов за сегодня")
    def get_counter_done_by_today(self):
        self.click_order_feed_button()
        self.scroll_to_bottom()
        return self.find_element(*Locators.DONE_BY_TODAY_COUNTER).text

    @allure.step("Делаем заказ")
    def create_order(self):
        self.find_element(*Locators.STELLAR_BURGER_LOGO).click()
        self.wait_for_element_to_be_clickable(Locators.FIRST_INGREDIENT_BUTTON)
        source = self.find_element(*Locators.FIRST_INGREDIENT_BUTTON)
        target = self.find_element(*Locators.TOP_INGREDIENT_TARGET)
        self.drag_and_drop(source, target)
        self.find_element(*Locators.PLACE_AN_ORDER_BUTTON).click()

    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account_button(self):
        self.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step("Клик по 'История заказов'")
    def click_order_history_button(self):
        self.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.ORDER_HISTORY)
        self.find_element(*Locators.ORDER_HISTORY).click()

    @allure.step("Получение номера заказа в Истории заказов")
    def get_order_ident_in_history(self):
        self.wait_for_element_to_be_visible(Locators.NUMBER_TOP_ORDER_IN_HISTORY)
        return self.find_element(*Locators.NUMBER_TOP_ORDER_IN_HISTORY).text

    @allure.step("Найти заказ в разделе 'Лента заказов'")
    def find_order_in_order_feed(self, order_number):
        xpath = self.create_xpath_by_text_in_feed(order_number)
        element = self.find_element_by_xpath(xpath)
        self.scroll_to_element(element)
        self.wait_for_element_to_be_visible_by_xpath(xpath)
        return element.is_displayed()
