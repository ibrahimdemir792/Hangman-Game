from project import dashes, guess_check, guess_letter
from unittest.mock import patch
import io
import pytest


def test_dashes():
    assert dashes("test", "e") == "_ e _ _"


def test_guess_check():
    assert guess_check("e", "test") == True
    assert guess_check("a", "test") == False


@patch("builtins.input", side_effect=["A", "b", "aa", "c"])
def test_guess_letter(mock_input):
    assert guess_letter() == "a"
    assert guess_letter() == "b"
    assert guess_letter() == "c"
