import pytest


@pytest.fixture
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture
def btn_selector():
    return "button"

@pytest.fixture
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture
def err():
    return "401"


@pytest.fixture
def hello_user():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture
def title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture
def descr_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture
def content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture
def save_btn():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""

@pytest.fixture
def title_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""