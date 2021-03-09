"""
作业：
1）完成企业微信app添加联系人
2）完成封装滑动查找

***注意事项***
1) 添加联系人时：怎么确定添加的姓名框确定是姓名那栏呢，就需要先找到姓名来填写
2）文本查找需要用contains,英文有些人开发会在后面加入空格
"""

import pytest
import yaml

from classWorks.app_tencent.index_page import IndexPage


class TestAppAddMember:
    @pytest.mark.parametrize('username, phone', yaml.safe_load(open('data/mamu_add_mem.yml', encoding='utf-8')))
    def test_add_member(self, username, phone):
        main = IndexPage(username=username, phone=phone)
        main.goto_address().add_member()