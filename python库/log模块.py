"""
log五级：debug,info,warning,error,critical
logging默认日志级别warning，
Handler对象负责分配合适的log信息(基于log信息的严重 程度)到handler指定的目的地.Logger对象可以用addHandler()方法添加零个或多个handler对象到它自身
"""

import logging

# log控制台输出
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# log文件输出
# logging.basicConfig(level=logging.INFO,
#                     filename='./temp/log.txt',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')



# 如果省略了name参数, getLogger将返回日志对象层次关系中的根Logger。
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = './temp/log.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')
