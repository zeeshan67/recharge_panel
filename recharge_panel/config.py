__author__ = 'vivaconnect'

from logClass import  Log
import os
import datetime
#Credentials


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config_logpath = os.path.join(BASE_DIR, 'recharge_panel')


myLog = Log()

def logging(log_file_name):
    strdate = datetime.datetime.now()
    log_path = os.path.join(config_logpath, str(strdate.year), str(strdate.month), str(strdate.day))
    if not (os.path.exists(log_path)):
        os.makedirs(log_path)

    loger_name = log_file_name + str(strdate.day) + '_' + str(strdate.month) + '_' + str(strdate.year)
    log = myLog.get_logger(loger_name)
    myLog.setup_logger(loger_name, log_path + '/' + str(log_file_name) + '.log')

    myLog.set_level(loger_name, 1)
    myLog.set_level(loger_name, 2)
    return log
