import allure
from helpers import URL


@allure.epic("Тестирование личного кабинета")
class TestAccountPage:

    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_transfer_to_personal_account_page(self, login, account_page):
        account_page.click_personal_account_button()
        assert account_page.get_current_url() == f"{URL}account/profile"

    @allure.title("Проверка перехода по клику на «История заказов»")
    def test_transfer_to_order_history(self, account_page, login):
        account_page.click_order_history_button()
        assert account_page.get_current_url() == f"{URL}account/order-history"

    @allure.title("Проверка выхода из аккаунта по кнопке «Выход»")
    def test_logout(self, account_page, login):
        account_page.click_logout_button()
        assert account_page.get_current_url() == f"{URL}login"
