from python_practice.python_commit_8_appPO.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()  #  实例化一个app
