import pytest


class TestCacultor:
  # @pytest.mark.parametrize("a, b, result", add_int_datas[0], ids=add_int_datas[1])
  @pytest.mark.add
  def test_add_int(self, get_instance, get_add_int_datas):
    # print(get_add_int_datas)
    data = get_add_int_datas
    assert data[2] == get_instance.add(data[0], data[1])


  @pytest.mark.add
  def test_add_float(self, get_instance, get_add_float_datas):
    data = get_add_float_datas
    assert data[2] == round(get_instance.add(data[0], data[1]), 2)


  @pytest.mark.div
  def test_div_normal(self, get_instance, get_div_normal_datas):
    assert get_div_normal_datas[2] == get_instance.div(get_div_normal_datas[0], get_div_normal_datas[1])


  @pytest.mark.div
  def test_div_error(self, get_instance, get_div_error_datas):
    with pytest.raises((ZeroDivisionError, TypeError)):
      get_div_error_datas[2] = get_instance.div(get_div_error_datas[0], get_div_error_datas[1])