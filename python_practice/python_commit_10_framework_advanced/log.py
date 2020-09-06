import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig()
log=logging.getLogger(__name__)
log.setLevel(logging.DEBUG) ## 设置日志级别为DEBUG，即只有日志级别大于等于DEBUG的日志才会输出