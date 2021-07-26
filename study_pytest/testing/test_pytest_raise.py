import pytest

def test_raise():
  with pytest.raises(ZeroDivisionError):
    1/0