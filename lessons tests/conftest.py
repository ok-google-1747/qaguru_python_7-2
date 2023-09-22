import pytest
from selene import browser


@pytest.fixture()
def open_browser():
    browser.open('https://www.google.ru/')


@pytest.fixture()
def browser_size(open_browser):
    browser.config.window_width = 1200

    browser.config.window_height = 830
