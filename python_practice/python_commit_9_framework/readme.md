# 测试框架改进——数据驱动基础封装1
把变化的东西都做成数据驱动

__数据驱动的应用__
- 测试数据的数据驱动
- PO定义的数据驱动
- 测试步骤的数据驱动
- 断言数据驱动

**不要全部框架数据驱动**
会丢失代码比较重要的重构、建模、开放的生态能力




__po模式封装的主要组成元素__
- page对象：完成对页面的封装
- driver对象（底层实现）：完成对web,android,ios,接口的驱动
- 测试用例（只关注PO，不需要关注框架底层那些变化的底层细节）：调用page对象实现业务并断言
- 数据封装：配置文件和数据驱动
- Utils：其他功能封装，改进原生框架不足

__自动化测试实践__
- 页面建模
- 测试框架改进
- 自动化用例组织
- 持续集成


__下一步问题思考__
为什么要二次封装测试框架？
- 升级弹框、广告弹框等
- 不同版本的控件id不一致
- 隐式等待太久
- case太多运行太慢
- 让使用门槛更低，让更多的人参与进来维护
从业务层面解决问题



============================================
PO的封装

-BasePage的封装
初始化方法、find方法、click方法、handle_exception方法
：把try catch放在底层实现里


__加入良好日志方便定位__
使用标准log取代print
logging.baseConfig(level=logging.DEBUG)
在具体的action中加入log方便追踪


__初始化顺序__
传统方式：
setup teardown与继承结合
setup_xxx teardown_xxx

pytest fixture风格：
fixture依赖关系
scope层级















