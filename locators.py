from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для фикстур
    LOGIN_BUTTON_ON_LOGIN_FORM = By.XPATH, "//button[text()='Войти']"
    EMAIL_FIELD_ON_LOGIN_FORM = By.XPATH, "//label[text() = 'Email']/parent::div//input"
    PASSWORD_FIELD_ON_LOGIN_FORM = By.NAME, "Пароль"
    PLACE_AN_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    # Локаторы для восстановления пароля
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    PASSWORD_RECOVERY_BUTTON = By.XPATH, "//a[text() = 'Восстановить пароль']"
    EMAIL_RECOVERY_FIELD = By.XPATH, "//label[text() = 'Email']/parent::div//input"
    SUBMIT_PASSWORD_RECOVERY_BUTTON = By.XPATH, "//button[text() = 'Восстановить']"
    PASSWORD_FIELD = By.XPATH, "//label[text() = 'Пароль']/parent::div//input"
    EYE_PICTURE = By.XPATH, "//div[@class = 'input__icon input__icon-action']"

    # Локаторы для личного кабинета
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text() = 'Личный Кабинет']"
    ORDER_HISTORY = By.XPATH, "//a[text() = 'История заказов']"
    LOGOUT_BUTTON = By.XPATH, "//button[text() = 'Выход']"

    # Локаторы для основного функционала
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text() = 'Конструктор']"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text() = 'Лента Заказов']"
    FIRST_INGREDIENT_BUTTON = By.XPATH, "//img[contains(@class, 'BurgerIngredient_ingredient__image__3e')][1]"
    INGREDIENT_DETAILS_WINDOW_HEADER = By.XPATH, "//h2[text() = 'Детали ингредиента']"
    INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]"
    TOP_INGREDIENT_TARGET = By.XPATH, "//span[text() = 'Перетяните булочку сюда (верх)']"
    FIRST_INGREDIENT_COUNTER = By.XPATH, "//p[contains(@class, 'counter_counter')][1]"
    ORDER_DETAILS_WINDOW_CLOSE_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"

    # Локаторы для раздела "Лента заказов"
    FIRST_ORDER_AREA = By.XPATH, "//ul[contains(@class, 'OrderFeed')]//a[1]"
    TOTAL_PRICE_OF_ORDER = By.XPATH, "//div[@class = 'Modal_priceBox__2U6_9']"
    ORDER_IDENT = By.XPATH, "//p[text() = 'идентификатор заказа']/parent::div/h2"
    LOADER = By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]"
    DONE_BY_ALL_TIME_COUNTER = By.XPATH, "//p[contains(@class, 'OrderFeed_number')][1]"
    DONE_BY_TODAY_COUNTER = By.XPATH, "//p[contains(@class, 'OrderFeed_number')][last()]"
    STELLAR_BURGER_LOGO = By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']"
    NUMBER_TOP_ORDER_IN_HISTORY = By.XPATH, "//ul[contains(@class, 'OrderHistory')]//p[@class = 'text text_type_digits-default'][1]"


