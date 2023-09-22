from selene.support.shared import browser
from selene import be, have


def test_search(open_browser, browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_bad_search(open_browser, browser_size):
    a = "0!fjkndv@#$][p243563#$%"
    browser.element('[name="q"]').should(be.blank).type(a).press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    print('Поиск не выдал результатов по введённому тексту: ' + a)
