import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser2():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver
    print("\nquit browser..")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def browser3(user_language=None):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser3 = webdriver.Chrome(options=options)
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    browser3 = webdriver.Firefox(firefox_profile=fp)