from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_url = (By.CSS_SELECTOR, '[href="/en-gb/accounts/login/"]')
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    b_button = (By.CSS_SELECTOR, '#add_to_basket_form [type="submit"]')
    item_name = (By.CSS_SELECTOR, '.row h1')
    # нужно пройти в корзину, чтобы взять селектор
    item_bname = (By.CSS_SELECTOR, '.alertinner>strong')
    item_price = (By.CSS_SELECTOR, 'p.price_color')
    total_price = (By.CLASS_NAME, '.alertinner p strong')
