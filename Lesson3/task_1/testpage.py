from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCR_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_TITLE_POST_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_BTN_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_FIELD_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label""")
    LOCATOR_FIELD_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label""")
    LOCATOR_FIELD_MESSAGE = (By.XPATH, """//*[@id="contact"]/div[3]/label""")
    LOCATOR_BTN_SAVE_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):


    def enter_login(self, word):
        logging.info('Enter login ')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)


    def enter_pass(self, word):
        logging.info('Enter password ')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)


    def click_login_btn(self):
        logging.info('Click button ')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()


    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        logging.info(f'Error {error_field.text} ')
        return error_field.text


    def check_user_name(self):
        name_field = self.find_element(TestSearchLocators.LOCATOR_HELLO_USER, time=2)
        logging.info(f'Error {name_field.text} ')
        return name_field.text


    def click_create_post_btn(self):
        logging.info('Click button create new post')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()


    def enter_title(self, text):
        logging.info('Enter title new post')
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(text)


    def enter_descr(self, text):
        logging.info('Enter description new post')
        descr_field = self.find_element(TestSearchLocators.LOCATOR_DESCR_FIELD)
        descr_field.clear()
        descr_field.send_keys(text)


    def enter_content(self, text):
        logging.info('Enter content new post')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(text)


    def click_save_post_btn(self):
        logging.info('Click button save new post')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()


    def check_title_post_field(self):
        title_post_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST_FIELD)
        logging.info(f'Error {title_post_field.text} ')
        return title_post_field.text


    def click_contact_us(self):
        logging.info('Click button contact us')
        btn = self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US)
        btn.click()


    def enter_name(self, word):
        logging.info('Enter name ')
        input1 = self.find_element(TestSearchLocators.LOCATOR_FIELD_NAME)
        input1.send_keys(word)


    def enter_email(self, word):
        logging.info('Enter email')
        input1 = self.find_element(TestSearchLocators.LOCATOR_FIELD_EMAIL)
        input1.send_keys(word)


    def enter_message(self, text):
        logging.info('Enter message')
        input1 = self.find_element(TestSearchLocators.LOCATOR_FIELD_MESSAGE)
        input1.send_keys(text)


    def save_contact_us(self):
        logging.info('Click button save message')
        btn = self.find_element(TestSearchLocators.LOCATOR_BTN_SAVE_CONTACT_US)
        btn.click()


    def check_alert(self):
        alert = self.driver.switch_to.alert
        logging.info(f'Error {alert.text} ')
        return alert.text
