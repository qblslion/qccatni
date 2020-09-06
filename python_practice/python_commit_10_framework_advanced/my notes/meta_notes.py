'''python元编程
一、元类是创建类的“类”
当我们定义一个类时，该类的对象都是由这个类来创建。但是类本身呢？类又是由什么来创建的呢？（当代杠精已上线）
这个问题就引申出元类的概念了，元类可以为其他类定义属性。
我们可以定义类来创建实例，而类，则是通过元类来创建。类是创建实例的蓝图，元类是创建类的蓝图

二、什么是元编程
软件开发中很重要的一条原则就是“不要重复自己的工作（Don’t repeat youself）”
也就是说当我们需要复制粘贴代码时候，通常都需要寻找一个更加优雅的解决方案，在python中，这类问题常常会归类为“元编程”

三、元编程的目的
创建函数和类，并用他们操作代码（例如修改，生成，或者包装自己已有的代码），尽可能地使代码优雅简洁。
具体而言，通过编程的方法，在更高的抽象层次上对一种层次的抽象的特性进行修改
    更多--https://www.cnblogs.com/gzl420/p/10915825.html
    
    数据驱动是为了让自己的框架更通用
'''''

# 验证1： type不仅仅是其他类型的元类，它也是它自己的元类
greeting="hello"
print(type(greeting))   # <class 'str'>    "hello"是个str类型
print(type(str))        # <class 'type'>   str 是个type类型
print(type(type))       # <class 'type'>   type 也是个type类型

#https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072 元类
#https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584 装饰器
#https://www.liaoxuefeng.com/wiki/1016959663602400/1017594591051072 类属性和实例属性

#https://www.jianshu.com/p/644d309b504e
