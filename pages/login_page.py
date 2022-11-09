from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='_login']"
    password_field_xpath = "//*[@id='_password']"
    sign_in_button_xpath = "//*[@id='_sign_in']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
