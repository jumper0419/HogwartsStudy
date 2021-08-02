from typing import List

import pytest
import sys
sys.path.append("../../")

from study_pytest.pythonencode.caculator import Cacultor
from study_pytest.pythonencode.handle_datas import HandleDatas

@pytest.fixture()
def get_instance():
  cacl:Cacultor = Cacultor()
  yield cacl

@pytest.fixture(params=HandleDatas.get_caculator_datas("add")[0], ids=HandleDatas.get_caculator_datas("add")[1])
def get_add_int_datas(request):
  yield request.param

@pytest.fixture(params=HandleDatas.get_caculator_datas("add", "float")[0],
                ids=HandleDatas.get_caculator_datas("add", "float")[1])
def get_add_float_datas(request):
  yield request.param

@pytest.fixture(params=HandleDatas.get_caculator_datas("div", "normal")[0])
def get_div_normal_datas(request):
  yield request.param

@pytest.fixture(params=HandleDatas.get_caculator_datas("div", "error")[0])
def get_div_error_datas(request):
  yield request.param


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
  # for item in items:
  #   item.name = item.name.encode("utf-8").decode("unicode-escape")
  #   item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
  items.reverse()

