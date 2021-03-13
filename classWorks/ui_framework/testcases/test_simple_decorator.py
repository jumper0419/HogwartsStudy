import pytest

from classWorks.ui_framework.pages.base_page import BasePage


def b(func):
    def run(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)
    return run

@b
def test_a():
    print("JSON")

def main():
    BasePage.a()

if __name__ == "__main__":
    # pytest.main(test_a)
    pytest.main(main)