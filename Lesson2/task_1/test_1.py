import time
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


# def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, err):
#
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#
#     err_label = site.find_element("xpath", x_selector3)
#     assert err_label.text == err
#
#
# def test_step2(x_selector1, x_selector2, btn_selector, hello_user):
#
#     input1 = site.find_element("xpath", x_selector1)
#     input1.clear()
#     input1.send_keys(testdata["user"])
#
#     input2 = site.find_element("xpath", x_selector2)
#     input2.clear()
#     input2.send_keys(testdata["pass"])
#
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     time.sleep(3)
#     elem = site.find_element("xpath", hello_user)
#     assert elem.text == f"Hello, {testdata['user']}"


def test_step3(x_selector1, x_selector2, btn_selector, title_selector,
               descr_selector, content_selector, save_btn, title_xpath):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["user"])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pass"])

    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(3)

    add_post_btn = site.find_element("css", btn_selector)
    add_post_btn.click()
    time.sleep(3)

    input3 = site.find_element("xpath", title_selector)
    input3.clear()
    input3.send_keys(testdata["title"])

    input4 = site.find_element("xpath", descr_selector)
    input4.clear()
    input4.send_keys(testdata["descr"])

    input5 = site.find_element("xpath", content_selector)
    input5.clear()
    input5.send_keys(testdata["content"])

    save_post_btn = site.find_element("xpath", save_btn)
    save_post_btn.click()
    time.sleep(3)

    elem = site.find_element("xpath", title_xpath)
    assert elem.text == testdata["title"]

    site.close()