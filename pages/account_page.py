import allure
from locators import Locators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account_button(self):
        self.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.ORDER_HISTORY)

    @allure.step("Клик по 'История заказов'")
    def click_order_history_button(self):
        self.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.ORDER_HISTORY)
        self.find_element(*Locators.ORDER_HISTORY).click()

    @allure.step("Клик по 'Выход'")
    def click_logout_button(self):
        self.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.LOGOUT_BUTTON)
        self.find_element(*Locators.LOGOUT_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.PASSWORD_RECOVERY_BUTTON)

