import allure
from locators import Locators
from pages.base_page import BasePage


class PassRecoveryPage(BasePage):

    @allure.step("Клик по 'Войти в аккаунт'")
    def click_login_button(self):
        self.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

    @allure.step("Клик по кнопке восстановления пароля")
    def click_pass_recovery_button(self):
        self.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()

    @allure.step("Заполнение email")
    def fill_email_field(self, email):
        self.wait_for_element_to_be_visible(Locators.EMAIL_RECOVERY_FIELD)
        self.find_element(*Locators.EMAIL_RECOVERY_FIELD).send_keys(email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def click_submit_button(self):
        self.find_element(*Locators.SUBMIT_PASSWORD_RECOVERY_BUTTON).click()
        self.wait_for_element_to_be_visible(Locators.PASSWORD_FIELD)

    @allure.step("Клик на кнопку отображения пароля")
    def click_eye_button(self):
        self.find_element(*Locators.EYE_PICTURE).click()

    @allure.step("Получение статуса отображения пароля")
    def get_field_status(self):
        return self.find_element(*Locators.PASSWORD_FIELD).get_attribute("type")
