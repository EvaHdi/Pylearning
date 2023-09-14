import logging
from logging import handlers
import time,os

class Logger():
    #The MAP of log relationship
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    # 1、设置存放日志目录，不存在则创建目录
    # 2、设置日志的级别'DEBUG','INFO', 'WARNING'，'ERROR'，'CRITICAL'
    # 3、设置写入日志的格式 '[%(asctime)s] [%(threadName)s] [line:%(lineno)d] %(levelname)s: %(message)s'
    # 4、设置控制台输出
    # 5、设置日志文件名
    # 6、确保每日生成不同日志文件，且能够区分日志生成时间，可用logging.handlers.TimedRotatingFileHandler进行处理，使用之前先进行导入
    # 7、将日志对象添加到logger里
    # 8、进行调用即可 get_logger(name="test")

    def __init__(self,filepath,filename):

        if os.path.isdir(filepath):
            pass
        else:
            os.mkdir(filepath)
        currrent_time = self.current_format_time.replace(":", "")

        filename = currrent_time+'-'+filename
        self.log_filename = os.path.join(filepath,filename)
        # print(self.log_filename)

        self.log_format_str = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        self.logger = logging.getLogger('Test')

        # log level
        self.level = 'debug'
        self.logger.setLevel(self.level_relations.get(self.level))

        #The handler is used to write log
        CMD_out= logging.StreamHandler()
        CMD_out.setFormatter(self.log_format_str) 
        
        file_out = logging.FileHandler(self.log_filename,encoding='utf-8')
        # file_out = handlers.TimedRotatingFileHandler(filename=self.log_filename,encoding='utf-8')
        file_out.setFormatter(self.log_format_str)

        # add target to logger
        self.logger.addHandler(CMD_out) 
        self.logger.addHandler(file_out)

    def logging_info(self,content):
        self.logger.info(content)

    def logging_warning(self,content):
        self.logger.warning(content)

    def logging_error(self,content):
        self.logger.error(content)
    
    def logging_debug(self,content):
        self.logger.debug(content)

    @property
    def current_format_time(self):
        return time.strftime('%Y-%m-%d-%X', time.localtime(time.time())).replace(";", "-")
if __name__ == '__main__':

    log = Logger()
    log.logger.debug('debug')
    log.logging_info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
