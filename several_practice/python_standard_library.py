#查看版本号
# import sys
# print(sys.version_info)

#将debug信息存起来
import os#os模块用以和操作系统交互
import platform#用以获取平台操作系统信息
import logging#记录信息
if platform.platform().startswith('Windows'):
    logging_file=os.path.join(os.getenv('HOMEDRIVE'),
                              os.getenv('HOMEPATH'),
                              'test,log')
else:
    logging_file=os.path.join(os.getenv('HOME'),
                              'test.log')
print('logging to',logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("start of the program")
logging.info("doing something")
logging.warning("Dying now")