from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

        link = self.browser.find_element(*MainPageLocators.login_link)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес??
        # Как именно определить правильность URL
        assert self.is_element_present(
            *LoginPageLocators.login_url), "Not correct login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.login_form), "Element isn't present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.register_form), "Element isn't present"
