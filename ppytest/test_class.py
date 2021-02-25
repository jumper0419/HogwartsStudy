from caculs.caculs import add


class TestClass:
    def test_add01(self):
        assert 30 == add(10, 20)

    def test_add02(self):
        assert 50 == add(2, 5)

    # TODO:
    def test_div(self):
        pass
