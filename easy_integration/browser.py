# Some shortcuts for common workflows in integration testing.

import atexit

from splinter.browser import Browser
from time import sleep

BROWSER = Browser('chrome')

def quit():
    BROWSER.quit()

def visit(path):
    return BROWSER.visit(app_url(path))

def app_url(path):
    return "http://127.0.0.1:8001" + path

def displays(text):
    return BROWSER.is_text_present(text)

def click(text):
    """Clicks the first button or link that matches the text.  Buttons have
    priority."""
    match = (BROWSER.find_by_value(text) or 
        BROWSER.find_link_by_text(text) or 
        BROWSER.find_by_css(text))
    return match.first.click()

def fill_in(name, value):
    BROWSER.fill(name, value)

def close():
    BROWSER.quit()

def select(select_id, option_text):
    BROWSER.select(select_id, option_text)

# When the program that imported this module terminates, close the
# web browser.
atexit.register(close)

