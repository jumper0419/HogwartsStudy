"""
作业：
1）完成企业微信app添加联系人
2）完成封装滑动查找
"""

import pytest
import yaml

from classWorks.app_tencent.index_page import IndexPage


class TestAppAddMember:
    @pytest.mark.parametrize('username, phone', yaml.safe_load(open('./data/mamu_add_mem.yaml', encoding='utf-8')))
    def test_add_member(self, username, phone):
        main = IndexPage(username=username, phone=phone)
        main.goto_address().add_member()