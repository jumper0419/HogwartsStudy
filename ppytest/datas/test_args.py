import pytest
import yaml

from caculs.caculs import add


def get_data():
    return yaml.safe_load(open('./datas.yaml'))


class TestArgs:
    datas = get_data()

    @pytest.mark.parametrize(['a', 'b', 'except_value'], datas['add'])
    def test_add(self, a, b, except_value):
        assert except_value == add(a, b)


    @pytest.mark.parametrize(['a', 'b', 'except_value'], datas['add'], ids=datas['ids'])
    def test_add2(self, a, b, except_value):
        assert except_value == add(a, b)

    @pytest.mark.skip
    def test_yaml(self):
        print(self.datas)