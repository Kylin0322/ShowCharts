#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 20210316(Yu):debug pass
# 20210806(Yu):debug pass


import logging
from logging.handlers import RotatingFileHandler
import sys

Main_log = "Main_log"
logger = logging.getLogger(Main_log)

rotating_log_conf = {"log_file_name": "debuglog.log",
                     "file_size": 1024*1024,
                     "backup_count": 2,
                     "formatter": '%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                     }


def config_2(a, G_debug_flag=False):
    if ("debug" in a) or G_debug_flag:
        # DEBUG INFO WARNING ERROR CRITICAL
        logging.basicConfig(level=logging.DEBUG,
                            filename='debuglog.log',
                            format='%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            )
        # format='%(asctime)s - (filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.debug("logging basicConfig finished,DEBUG")
        logging.debug(a)
    else:
        # DEBUG INFO WARNING ERROR CRITICAL
        logging.basicConfig(level=logging.INFO,
                            filename='debuglog.log',
                            format='%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            )
        # format='%(asctime)s - (filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logging.debug("logging basicConfig finished,INFO")
        logging.debug(a)


def config_1(a, G_debug_flag=False):
    '''waiting for debug
    '''
    if ("debug" in a) or G_debug_flag:
        # DEBUG INFO WARNING ERROR CRITICAL
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        RH = RotatingFileHandler(
            filename=r"debuglog.log", maxBytes=1024, backupCount=2)
        RH.setFormatter('%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        logger.addHandler(RH)
        logger.debug("logging basicConfig finished,DEBUG")
        logger.debug(a)
    else:
        # DEBUG INFO WARNING ERROR CRITICAL
        # logging.basicConfig(level=logging.INFO,
        #                    filename='debuglog.log',
        #                   format='%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s',
        #                    )
        # format='%(asctime)s - (filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        RH = RotatingFileHandler(
            filename=r"debuglog.log", maxBytes=1024, backupCount=2)
        RH.setFormatter('%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        logger.addHandler(RH)
        #logging.debug("logging basicConfig finished,DEBUG")
        # logging.debug(a)


def config(debug_flag=False):
    ''' rotate log function, test ok
        main: logger = logging.getLogger(Main_log)
              config(True)

        sub: logger = logging.getLogger(Main_log)
    '''
    # Log to file
    logger = logging.getLogger(Main_log)
    if debug_flag:
        log_level = logging.DEBUG       # FATAL CRITICAL ERROR WARNING INFO DEBUG
    else:
        log_level = logging.ERROR

    logger.setLevel(level=log_level)  # FATAL CRITICAL ERROR WARNING INFO DEBUG
    # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
    rHandler = RotatingFileHandler(filename="debuglog.log", maxBytes=1024*1, backupCount=2)
    rHandler.setLevel(log_level)
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s-%(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    rHandler.setFormatter(formatter)

    logger.addHandler(rHandler)

    # 控制台输出log
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)

    # 控制台输出log
    # logger.addHandler(console)


if __name__ == '__main__':
    print("P1 test data -------------")
    logger = logging.getLogger(Main_log)
    # a.append("debug")
    # config(a)
    # config(a, True)
    # config_1(a)
    # config_1(a, True)
    # Aug 06
    config(True)
    logger = logging.getLogger(Main_log)
    logger.debug("Log level test debug")
    logger.info("Log level test info")
    logger.warning("Log level test warning")
    logger.error("Log level test error")
    # for i in range(1000):
    #logging.debug(str(i) + "logging basicConfig finished,DEBUG")
    #logger.debug(str(i) + "logging basicConfig finished,DEBUG")

    print("P1 test data -------------")
