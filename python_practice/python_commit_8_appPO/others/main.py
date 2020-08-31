from python_practice.python_commit_8_appPO.others.base_page_backup import BasePageBackup


class Main(BasePageBackup):
    def goto_search(self):
        self.steps("./test.yaml") # 直接传入文件路径就能实现完成解析
        # testcase 可以不变
        # 例如app=App()
        # app.start().main().goto_search() 依然会调用Main方法里面的goto_search()
        #从而执行BasePageBackup类中的解析