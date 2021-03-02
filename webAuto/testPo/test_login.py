from webAuto.login_page.main_page import MainPage


class TestLogin:
    def test_login(self):
        main = MainPage()
        print(main.goto_login().scan())