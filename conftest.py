import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="function")
def browser2():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver
    print("\nquit browser..")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language: en, ru, etc.")

@pytest.fixture(scope="function")
def browser3(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if user_language:
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if user_language:
            options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    browser.quit()