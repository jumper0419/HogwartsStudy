import pytest

import sys
sys.path.append("../../")
from study_pytest.pythonencode.caculator import Cacultor


class TestCacultor:
  def setup(self):
    self.cacl:Cacultor = Cacultor()

  @pytest.mark.parametrize("a, b, result", [(1, 1, 2), (100, 200, 300)])
  def test_add(self, a, b, result):
    assert result == self.cacl.add(a, b)