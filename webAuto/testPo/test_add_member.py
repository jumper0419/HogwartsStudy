# -*- coding: utf-8 -*-
import pytest
import yaml

from webAuto.address_page.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize('username, phone, acctid', yaml.safe_load(open('./add_member.yaml', encoding='utf-8')))
    def test_add_member(self, username, phone, acctid):
        main = MainPage(username, phone, acctid)
        main.goto_address().goto_add_member()