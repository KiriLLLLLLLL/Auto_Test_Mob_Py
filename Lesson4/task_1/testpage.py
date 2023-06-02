import yaml, requests
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
from zeep import Client, Settings

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):


    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True


    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text


    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True


#ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], text, description="Title form")

    def enter_descr(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCR_FIELD"], text, description="Description form")

    def enter_content(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], text, description="Content form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_NAME"], word, description="Name field")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_EMAIL"], word, description="Email field")

    def enter_message(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FIELD_MESSAGE"], text, description="Message field")

#GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error 401")


    def get_user_name(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO_USER"], description="username")

    def get_title_post_field(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_TITLE_POST_FIELD"], description="post title")

    def get_alert(self):
        alert = self.get_alert_text()
        logging.info(f'Error {alert} ')
        return alert

#CLICK BUTTON

    def click_save_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save new post")

    def click_contact_us(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CONTACT_US"], description="contact us")

    def click_save_contact_us(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_SAVE_CONTACT_US"], description="send message to us")

    def click_create_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="create new post")

    def click_login_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")


class RestApiTest:



    def get_someone_post(self, token):
        try:
            g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token},
                             params={'owner': 'notMe'})
            listcont = [i['title'] for i in g.json()['data']]
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We find text {listcont} in field {g.json()}")
        return listcont

    def add_new_post(self, token):
        with open("testdata.yaml") as f:
            user = yaml.safe_load(f)
        try:
            response = requests.post("https://test-stand.gb.ru/api/posts", headers={'X-Auth-Token': token},
                                     data={'title': user['title'],
                                           'description': user['descr'],
                                           'content': user['content']})
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We are creating a new post {response.json()}")
        return response.json()

    def get_my_post(self, token):
        try:
            response = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
            listdesc = [i['description'] for i in response.json()['data']]
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We getting description new post {listdesc}")
        return listdesc

    def checkText(self, word):
        with open('testdata.yaml') as f:
            wsdl = yaml.safe_load(f)['wsdl']

        settings = Settings(strict=False)
        client = Client(wsdl=wsdl, settings=settings)

        try:
            response = client.service.checkText(word)[0]['s']
        except:
            logging.exception("Find element exception")
            response = None
        return response