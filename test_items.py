import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_link(language):
    return f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"


def test_should_have_add_to_cart_button(request, browser3):
    user_language = request.config.getoption("language")
    if user_language is None:
        pytest.skip("Skipping test because language is not specified")

    link = get_link(user_language)
    browser3.get(link)
    time.sleep(10)
    button = WebDriverWait(browser3, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    )
    assert button is not None


@pytest.mark.parametrize('language', ['en-gb', 'ru'])
def test_should_have_add_to_cart_button_param(request, browser3, language):
    user_language = request.config.getoption("language")
    # Пропускаем параметризованный тест, если язык указан явно
    if user_language is not None:
        pytest.skip("Skipping param test because language is specified in command line")

    # Устанавливаем язык, не используя предпочитаемый язык из конфигурации
    link = get_link(language)
    browser3.get(link)
    time.sleep(10)
    button = WebDriverWait(browser3, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    )
    assert button is not None
