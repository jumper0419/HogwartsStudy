import pytest

list = [1, 2]

class TestSetup:
  def setup(self, list=list):
    for item in list:
      print(item)

  def test_a(self):
    print("aaaa")