import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("  skypro  ", "skypro  "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    (None),
    (123),
    ([1, 2, 3]),
])
def test_capitalize_negative_invalid_type(invalid_input):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.capitalize(invalid_input)


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    (123),
    (None),
    ([1, 2, 3]),
])
def test_trim_negative_invalid_type(invalid_input):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.trim(invalid_input)


@pytest.mark.negative
@pytest.mark.parametrize("invalid_string, symbol", [
    (123, "S"),
    (None, "S"),
    (3.14, "S"),
])
def test_contains_negative_invalid_string(invalid_string, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(invalid_string, symbol)


@pytest.mark.negative
@pytest.mark.parametrize("invalid_string, symbol", [
    (123, "S"),
    (None, "S"),
    (3.14, "S"),
])
def test_delete_symbol_negative_invalid_string(invalid_string, symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(invalid_string, symbol)
