import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    #if browser == 'headless':
    else:
        # print("Headless mode")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options= chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  #
    driver.quit()


def pytest_metadata(metadata):
    metadata["Project Name"] = "Binder_Amazon"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Girish Kadam"
    metadata.pop("Plugins", None)


@pytest.fixture(params=[

    ("Girishkadam1819@gmail.com", "Girish@1819", "Pass"),
    ("TestUser101@gmail.com", "Test123", "Fail"),
    ("TestUser101@gmail.com", "Test1231", "Fail"),
    ("TestUser101@gmail.com", "Test1231", "Fail")

])
def getDataForLogin(request):
    return request.param
