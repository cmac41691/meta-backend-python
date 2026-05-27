import addition
import pytest


def test_add():
    assert addition.add(4, 3) == 7


def test_sub():
    assert addition.sub(5, 1) == 4