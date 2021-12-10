from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class ProductPage(BasePage, ProductPageLocators):

    def add_item(self):
        '''
        Описать метод добавления в корзину.    
        '''

        try:
            self.browser.implicitly_wait(5)
            b_button = self.browser.find_element(*ProductPageLocators.b_button)
            b_button.click()
        except NoSuchElementException:
            print("Basket element not found")
        # активация скидки

        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert appeared")

    def naming_equality(self):
        '''
        Проверка совпадения названия добавленного товара и товара в корзине.
        '''
        assert self.item_name == self.item_bname, 'Naming is the same'

    def check_price_equality(self):
        '''
        Проверка стоимости товара со стоимостью корзины. 
        '''
        assert self.item_price == self.total_price, 'Price is the same'
