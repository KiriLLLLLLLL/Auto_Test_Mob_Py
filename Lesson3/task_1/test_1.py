import yaml, time
from testpage import OperationsHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# def test_step1(browser, err):
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login("test")
#     testpage.enter_pass("test")
#     testpage.click_login_btn()
#     assert testpage.get_error_text() == err
#
#
# def test_step2(browser):
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata["user"])
#     testpage.enter_pass(testdata["pass"])
#     testpage.click_login_btn()
#     assert testpage.check_user_name() == f"Hello, {testdata['user']}"


def test_step3(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["user"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_btn()

    testpage.click_create_post_btn()

    testpage.enter_title(testdata["title"])
    testpage.enter_descr(testdata["descr"])
    testpage.enter_content(testdata["content"])

    testpage.click_save_post_btn()
    time.sleep(2)

    assert testpage.check_title_post_field() == testdata["title"]


def test_step4(browser, err2):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_contact_us()
    testpage.enter_name(testdata["name"])
    testpage.enter_email(testdata["email"])
    testpage.enter_message(testdata["message"])
    testpage.save_contact_us()
    time.sleep(2)
    assert testpage.check_alert() == err2