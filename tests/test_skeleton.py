# -*- coding: utf-8 -*-

import pytest

from t02.skeleton import fib

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)