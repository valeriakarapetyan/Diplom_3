import allure


@allure.epic("Тестирование раздела 'Лента заказов'")
class TestOrderFeedPage:

    @allure.title("Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_model_window_by_click_on_order_in_feed(self, order_feed_page):
        order_feed_page.click_order_feed_button()
        order_feed_page.click_on_first_order_in_feed()
        assert order_feed_page.check_order_details_window_in_feed_is_open() == True

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе В работе")
    def test_user_order_is_presented_in_process(self, create_an_order, order_feed_page):
        ident = order_feed_page.get_order_ident()
        order_feed_page.close_order_info_window()
        order_feed_page.click_order_feed_button()
        assert order_feed_page.find_order_in_progress(ident) == True

    @allure.title("Проверка, что при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_making_an_order_increases_all_time_counter(self, login, order_feed_page):
        first_value = order_feed_page.get_counter_done_by_all_time()
        order_feed_page.create_order()
        second_value = order_feed_page.get_counter_done_by_all_time()
        assert first_value < second_value

    @allure.title("Проверка, что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_making_an_order_increases_today_counter(self, login, order_feed_page):
        first_value = order_feed_page.get_counter_done_by_today()
        order_feed_page.create_order()
        order_feed_page.close_order_info_window()
        second_value = order_feed_page.get_counter_done_by_today()
        assert first_value < second_value

    @allure.title("Проверка, что заказы из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_orders_from_order_history_shows_in_order_feed(self, create_an_order, order_feed_page):
        order_feed_page.close_order_info_window()
        order_feed_page.click_personal_account_button()
        order_feed_page.click_order_history_button()
        order_number = order_feed_page.get_order_ident_in_history()
        order_feed_page.click_order_feed_button()
        return order_feed_page.find_order_in_order_feed(order_number) == True
