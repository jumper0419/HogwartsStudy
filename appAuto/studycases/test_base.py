# -*- encoding: UTF-8 -*-
from time import sleep

from appAuto.studycases.base import Base


class TestApp(Base):
    def test_fist_app(self):
        sleep(1)
        self.driver.find_element_by_id("com.android.chrome:id/search_box_text").send_keys("alibaba")
        sleep(3)