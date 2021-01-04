import pytest

from string_calculator import add, split_string, parse_custom_separator, has_custom_separator

testdata = [
    ("", 0),
    ("1", 1),
    ("2", 2),
    ("1,1", 2),
    ("2,1", 3),
    ("2,1,2", 5),
    ("1\n2,3", 6),
    ("2,2\n3", 7),
]


@pytest.mark.parametrize("string, expected", testdata)
def test_add_sting(string, expected):
    assert add(string) == expected


def test_complex_separator():
    assert add("//;\n1;2") == 3


def test_extract_separator():
    separator, _ = split_string("//;\n1;2")
    assert separator == ";"


def test_extract_separator2():
    separator, _ = split_string("1,2")
    assert separator == ","


def test_parse_custom_separator():
    assert ";" == parse_custom_separator("//;")


def test_has_custom_separator():
    parts = "//;\n1;2".split("\n")
    assert has_custom_separator(parts) is True


def test_extract_string():
    _, string = split_string("//;\n1;2")
    assert string == "1;2"


def test_extract_separator():
    separator, _ = split_string("//;\n1;2")
    assert separator == ";"


def test_extract_string2():
    _, string = split_string("1,2")
    assert string == "1,2"


def test_numbers_bigger_than_1000_should_be_ignored():
    assert add("2,1001") == 2