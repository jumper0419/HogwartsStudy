from caculs.caculs import add, div


def setup_module():
    print("run setupModule")


def teardown_module():
    print("run teardownModule")


def setup_function():
    print("run setupFunction")


def teardown_function():
    print("run teardownFunction")


class TestDemo:

    def setup_class(self):
        print("run setupClass")


    def teardownClass(self):
        print("run teardownClass")

    def setup(self):
        print("run setup")


    def teardown(self):
        print("run teardown")


    def test_add(self):
        print("我是add方法")
        assert 90 == add(40, 50)


    def test_div(self):
        assert 3.0 == div(9, 3)


class TestDemo02:
    def test_div(self):
        assert 3 == div(9, 3)


def test_pr():
    print("我是函数")