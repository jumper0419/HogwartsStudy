"""
作业：利用 PO 封装添加成员
解题思路：
步骤一：先采用PO模式封装好企业微信的首页和通讯录页
1）封装首页，需要实现去通讯录的功能
2）封装通讯录页，需要实现添加成员的功能

步骤二：测试添加成员
1）实现首页的实例化，然后通过实例化对象进行调用

"""
import pytest
import yaml

from classWorks.address_page.index_page import IndexPage


class TestAddMember:
    @pytest.mark.parametrize('username, phone, acctid', yaml.safe_load(open('data/add_member.yml', encoding='utf-8')))
    def test_add_member(self, username, phone, acctid):
        index = IndexPage(username=username, phone=phone, acctid=acctid)
        index.goto_address().add_member()