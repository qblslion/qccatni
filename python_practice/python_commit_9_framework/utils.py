

#   封装常见的 不好分类的工具
import yaml


class Utils:
    #  load一个yaml文件，把数据读进来
    @classmethod
    def from_file(cls, path):
        with open(path,encoding='utf-8') as f:
            yaml_data=yaml.safe_load(f)  #  生成所有数据
            params=yaml_data['params'] # 取数据 有三项数据
            keys = set() # 定义一个集合，去重
            values=[]
            if isinstance(params, list):
                # keys= [row.keys() for row in params].extend() #  每一行是个kv结构的字典
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key)  #  取出所有的key,如果是多个参数是逗号隔开的
                            print(values)
                            # values.append(row.values()) # data['values']=[dict_values(['alibaba']), dict_values(['baidu']), dict_values(['jd'])]
                            # values.append(list(row.values())) # [['alibaba'], ['baidu'], ['jd']],生成的pytest结构集 keyword0,keyword1,keyword2
                            values.append(list(row.values())[0]) # data['values']=['alibaba', 'baidu', 'jd']

                        # keys+=row.keys() # 这时候keys是所有的数据
                        # for key in row.keys():
                        #     keys.append(key)
                # keys = [row.keys() for row in params].extend()
            var_names=','.join(keys) # 取出参数化的名字,keys
            # var_names=keys  #  AttributeError: 'set' object has no attribute 'split'
            # var_values=row
            res={'keys': var_names, 'values':values}
            return res