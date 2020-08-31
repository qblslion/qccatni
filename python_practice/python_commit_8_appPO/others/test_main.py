import pytest
import yaml

from python_practice.python_commit_8_appPO.others.test_base import TestBase

# a simple demo
#  断言截图

# 继承TestBase
class TestMain(TestBase):

    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self):
        self.app.start().goto_main_page().goto_contact()
        print(1111)
        print(2222)
        assert 1 == 1

    def test_window(self):
        self.app.start().goto_main_page()