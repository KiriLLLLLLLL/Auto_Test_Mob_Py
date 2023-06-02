import logging
from testpage import RestApiTest


def test_step5(good, bad):
    logging.info("Test5 Starting")
    result = RestApiTest()
    assert good in result.checkText(bad)


def test_step6(login, text1):
    logging.info("Test6 Starting")
    result = RestApiTest()
    assert text1 in result.get_someone_post(login)


def test_step7(login, checking_description):
    logging.info("Test7 Starting")
    result = RestApiTest()
    result.add_new_post(login)
    assert checking_description in result.get_my_post(login)