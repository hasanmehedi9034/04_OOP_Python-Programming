import pytest
import time
import pytest_html

def make_upper(string):
    return string.upper()

def make_capital(string):
    return string.capitalize()

def make_lower(string):
    return string.lower()

def test_script():
    assert make_upper('mehedi') == 'MEHEDI'
    assert make_capital('mehedi') == 'Mehedi'
    assert make_lower('MEHEDI') == 'mehedi'
