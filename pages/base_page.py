import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Делаем Xpath по тексту в блоке В работе")
    def create_xpath_by_text_in_history(self, ident):
        xpath = f"//ul[contains(@class, 'orderListReady')]//li[contains(., '{ident}')]"
        return xpath

    @allure.step("Делаем Xpath по тексту в Ленте заказов")
    def create_xpath_by_text_in_feed(self, ident):
        xpath = f"//ul[contains(@class,'OrderFeed')]//p[contains(., '{ident}')]"
        return xpath

    @allure.step("Ищем элемент по xpath")
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    @allure.step("Ждем элемент по xpath")
    def wait_for_element_to_be_visible_by_xpath(self, xpath, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step("Ищем элемент по локатору")
    def find_element(self, *element):
        return self.driver.find_element(*element)

    @allure.step("Ждем, пока элемент будет виден")
    def wait_for_element_to_be_visible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))

    @allure.step("Ждем, пока элемент будет кликабелен")
    def wait_for_element_to_be_clickable(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    @allure.step("Клик по элементу с использованием JS")
    def click_by_js(self, button):
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Ждем, пока элемент исчезнет")
    def wait_for_element_to_disappear(self, element):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located(element))

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получаем текущий адрес")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("ДрагнДроп")
    def drag_and_drop(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
