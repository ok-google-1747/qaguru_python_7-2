import pytest
from selene import browser


@pytest.fixture(autouse=True)
def open_browser(browser_size):
    browser.open('https://www.google.ru/')


@pytest.fixture()
def browser_size():
    browser.config.window_width = 1200

    browser.config.window_height = 830
