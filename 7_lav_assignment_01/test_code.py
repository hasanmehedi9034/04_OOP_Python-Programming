import pytest
import time
import pytest_html

def make_upper(string):
    return string.upper()

def make_capital(string):
    return string.capitalize()

def make_lower(string):
    return string.lower()

def test_make_upper():
    assert make_upper('mehedi') == 'MEHEDI'

def test_make_capital():
    assert make_capital('mehedi') == 'Mehedi'

def test_make_lower():
    assert make_lower('MEHEDI') == 'mehedi'


# def test_script():
#     test_make_upper()
#     test_make_capital()
#     test_make_lower()
