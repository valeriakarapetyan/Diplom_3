import allure
from helpers import URL


@allure.epic("Тестирование восстановления пароля")
class TestPassRecoveryPage:

    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transfer_to_recovery_page(self, pass_recovery_page):
        pass_recovery_page.click_login_button()
        pass_recovery_page.click_pass_recovery_button()
        assert pass_recovery_page.get_current_url() == f"{URL}forgot-password"

    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_input_email_and_submit(self, pass_recovery_page):
        pass_recovery_page.click_login_button()
        pass_recovery_page.click_pass_recovery_button()
        pass_recovery_page.fill_email_field('Test_email')
        pass_recovery_page.click_submit_button()
        assert pass_recovery_page.get_current_url() == f"{URL}reset-password"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_on_eye_makes_field_active(self, pass_recovery_page):
        pass_recovery_page.click_login_button()
        pass_recovery_page.click_pass_recovery_button()
        pass_recovery_page.fill_email_field('Test_email')
        pass_recovery_page.click_submit_button()
        pass_recovery_page.click_eye_button()
        status = pass_recovery_page.get_field_status()
        assert status == 'text'
