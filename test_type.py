import pytest
from type_test import add

def test_add():
    assert add(5, 10) == 15
    assert add("Hello, ", "World!") == "Hello, World!"
    assert add(3.5, 2.5) == 6.0
    assert add("cat", 1) == "cat1"    