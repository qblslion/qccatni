
'''
如何让测试框架丰富起来？
第一个维度，测试步骤的数据驱动
比如写在yaml里，平台的数据库里，让测试框架自动去导
第二个维度，测试数据的数据驱动
第三个维度，PO的数据驱动
'''
'''
1.str.join(sequence)
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
" ".join(str), join分割的必须是字符串,字符串数组和列表都可以，但是不能含有数字等

print('-'.join("habit"))       #  h-a-b-i-t
print('-'.join(["a","b","c"])) #  a-b-c



2.list.append() append只能传入一个参数，所以会把参数作为一个整体追加到原列表之后。
                append 该方法无返回值，但是会修改原来的列表
                
  list.extend() extend相当于列表的相加。extend 该方法没有返回值，但会在已存在的列表中添加新的列表内
  体会：list.append('hello')整体追加   和 list.extend('hello')  拆分追加 的区别
  
  
  test1=[1,2,3]
  test2=["a","n"]
  print(test1.append([5])) # None
  test2.append([5,6][0]) # 追加[5,6]这个列表的第一个元素
  print(test2)  # ['a', 'n', 5]
  
3.d={'k1':123,'k2':456,'k3':'abc'}
a=d.keys()    
print(a)          #  dict_keys(['k1', 'k2', 'k3'])
print(list(a))    #  ['k1', 'k2', 'k3']
print(list(a)[0]) # k1
print(type(a))    #  <class 'dict_keys'>
b=d.values()
print(b)          #  dict_values([123, 456, 'abc'])
print(type(b))    #  <class 'dict_values'>


4.aaaa={"alibaba","jd","baidu"}
print(aaaa)            #  {'jd', 'alibaba', 'baidu'}
print(','.join(aaaa))  #  jd,alibaba,baidu   打印结果看出，字符串的引号会被直接去掉


5.dic1={'ka':1,'kb':2,'kc':3}
print(dic1.items())         #  dict_items([('ka', 1), ('kb', 2), ('kc', 3)])
print(list(dic1.items()))   #  dict_keys(['ka', 'kb', 'kc'])
print(dic1.keys())          #  dict_values([1, 2, 3])
print(dic1.values())
for k,v in dic1.items():
    print('k,v',k,v)       #k,v ka 1
                            k,v kb 2
                            k,v kc 3

'''


##测试用例
import pytest

from python_practice.python_commit_9_framework.demo_po_page import DemoPage
from python_practice.python_commit_9_framework.utils import Utils


class TestLogin:
    # 在类初始化的时候读数据
    data=Utils.from_file('./test_search.yaml')  # 把返回结果存到变量data里

    def setup_class(self):  #  setup_class只执行一次，但是search出来有3个case,所有case都要先执行self.demo.start()
        self.demo = DemoPage()
        self.demo.start()   #  别忘了启动


    def setup(self):  #  每个case执行之前都要执行
        pass

    def teardown(self): # 每个case 执行完之后都要执行
        self.demo.back()  # 点了取消这个按钮,不是后退
        return self

    def teardown_class(self):
        self.demo.stop()

    # #  一个参数化的用例
    # #  to do:测试数据的数据驱动
    @pytest.mark.parametrize('username, password',[
        ('user1','pwd1'),
        ('user2','pwd2')
    ])
    def test_login(self, username, password):
        # to do:测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1==1

    # @pytest.mark.parametrize('keyword',[
    #     'alibaba'
    #     # 'baidu',
    #     # 'jd'
    # ])
    #  通过读数据文件，读出三条数据，动态化地传递进来
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self, keyword):
        print(self.data)
        print(self.data['keys'])
        print(self.data['values'])
        print(keyword)
        # print(self.data)
        # print(keyword)
        self.demo.serach(keyword)


