import pytest


@pytest.mark.parametrize("name", [["哈利"], ["何敏"]], ids=["哈利", "何敏"])
def test_demo(name):
  print(name)