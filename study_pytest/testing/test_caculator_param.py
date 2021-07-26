import pytest
import sys
import yaml
sys.path.append("../../")
from study_pytest.pythonencode.caculator import Cacultor


def get_param_datas(name, type="int"):
  with open("./datas/caculator.yml", encoding='utf-8') as f:
    all_datas = yaml.safe_load(f)
  datas = all_datas[name][type]["datas"]
  ids = all_datas[name][type]["ids"]
  return (datas, ids)

class TestCacultor:
  add_int_datas = get_param_datas("add", "int")
  add_float_datas = get_param_datas("add", "float")
  div_normal_datas = get_param_datas("div", "normal")
  div_error_datas = get_param_datas("div", "error")

  def setup(self):
    self.cacl:Cacultor = Cacultor()

  @pytest.mark.parametrize("a, b, result", add_int_datas[0], ids=add_int_datas[1])
  def test_add_int(self, a, b, result):
    assert result == self.cacl.add(a, b)

  @pytest.mark.parametrize("a, b, result", add_float_datas[0], ids=add_float_datas[1])
  def test_add_float(self, a, b, result):
    # assert result == self.cacl.add(a, b)
    assert result == round(self.cacl.add(a, b), 2)

  @pytest.mark.parametrize("a, b, result", div_normal_datas[0])
  def test_div_normal(self, a, b, result):
    assert result == self.cacl.div(a, b)

  @pytest.mark.parametrize("a, b, result", div_error_datas[0])
  def test_div_error(self, a, b, result):
    with pytest.raises((ZeroDivisionError, TypeError)):
      self.cacl.div(a, b)