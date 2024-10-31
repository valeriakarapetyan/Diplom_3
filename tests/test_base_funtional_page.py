import allure
from helpers import URL


@allure.epic("Тестирование основного функционала")
class TestBaseFunctionalPage:

    @allure.title("Проверка перехода на главную страницу по кнопке «Конструктор»")
    def test_transfer_to_constructor(self, base_functional_page):
        base_functional_page.click_constructor_button()
        assert base_functional_page.get_current_url() == URL

    @allure.title("Проверка перехода на ленту заказов по кнопке «Лента заказов»")
    def test_transfer_to_order_feed(self, base_functional_page):
        base_functional_page.click_order_feed_button()
        assert base_functional_page.get_current_url() == f"{URL}feed"

    @allure.title("Проверка открытия окна с деталями ингредиентов при клике по ингредиенту")
    def test_click_on_ingredient_shows_overlay_window(self, base_functional_page):
        base_functional_page.click_on_ingredient()
        assert base_functional_page.check_order_details_window_is_open() == True

    @allure.title("Проверка закрытия окна с деталями ингредиентов при клике по крестику")
    def test_click_on_close_button_closes_ingredient_window(self, base_functional_page):
        base_functional_page.click_on_ingredient()
        base_functional_page.click_close_button_on_ingredient_details_window()
        assert base_functional_page.check_order_details_window_is_open() == False

    @allure.title("Проверка увеличения значения каунтера ингредиента после перетаскивания в заказ")
    def test_dragging_ingredient_increase_counter(self, base_functional_page):
        base_functional_page.drag_ingredient_to_order()
        assert base_functional_page.get_counter_value() == '2'

    @allure.title("Проверка, что залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, base_functional_page, login):
        base_functional_page.drag_ingredient_to_order()
        base_functional_page.click_place_order()
        assert base_functional_page.check_order_details_window_is_open() == True

