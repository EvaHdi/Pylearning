#coding: utf-8
####################################################################################################################
##
##  Unpublished Confidential Information of Teledyne Lecroy.
##  Do not disclose.
##  Copyright (c) 2022 Teledyne Lecroy.  All Rights Reserved.
##
##  The contents of this software are proprietary and confidential to
##  Teledyne Lecroy and are limited in distribution to those with
##  a direct need to know.  Individuals having access to this software are
##  responsible for maintaining the confidentiality of the content and for
##  keeping the software secure when not in use.  Transfer to any party is
##  strictly forbidden other than as expressly permitted in writing by
##  Teledyne Lecroy.
##
#####################################################################################################################

import os,time,sys
from OakGateSupportTools.Libs.LoggingUtils import LoggingUtils
import logging
'''
@Functions  : LOG APIs for Oakgate
@Author     : Peter.Sun@longsys.com
@ChangeList : 
                @2022/6/9   <Version 1.0>-- Add Initial Log Operation API
                @2022/6/10  <Version 1.1>-- Support timestamp for each log
                @2022/6/12  <Version 1.2>-- Support caller function/line number get and log
'''

LOG_DEBUG = True

class LOG_API():
    ''' LOG API
    
    Logging APIs
        Logging to files with specific format.
    
    Methods:
        Log
        GetLocalTimeString
        DeInitialize
        
    Attributes:
        None
    '''
    def __init__(self, logPath = './', logFileName = "default.log"):
        '''Init Log Class
        
        Initialize Log Class.
        
        Args:
            logPath : Log File Path
            logFileName : Log File Name
        Returns:
        '''
        self.logPathFull = logPath
        if False == os.path.isdir(self.logPathFull):
            os.makedirs(self.logPathFull)

        if False == os.path.isdir(self.logPathFull):
            self.logPathFull = os.path.dirname(os.path.realpath(__file__))
        
        print("*\t*Info: logging base path:", self.logPathFull)
        
        # self.initTime = (time.strftime('%Y-%m-%d-%X', time.localtime(time.time())).replace(";", "-")).replace(":", "")
        self.initTime = time.strftime('%Y-%m-%d %X', time.localtime(time.time())).replace(";", "-")

        print("*\t*Info: {} start record test log in {}:".format(self.initTime,self.logPathFull))
        self.infostring = "*\t*Info: {} start record test log".format(self.initTime)
        self.logFileName = logFileName
        self.logFilePathName = os.path.join(self.logPathFull, self.logFileName)
        print("*\t*Info: self.logFilePathName is {} :".format(self.logFilePathName))
        
        if os.path.isfile(self.logFilePathName):
            os.remove(self.logFilePathName)

        self.__InitLog(self.logFilePathName, self.infostring)
        
        # Create the console log file
        self.LoggingService = LoggingUtils()
        
        # self.ConsoleLog_txt_FileObject = self.LoggingService.openTextFile(logPath, "OGT-" + logFileName)
        
    def __InitLog(self, logFile, logString):
        '''Init Log
        
        Initialize Log Module.
        
        Args:
        Returns:
        '''
        self.logfileOperator = open(logFile, 'a+')
        self.logfileOperator.write(logString + "\n")
            
    def Log(self, *logString):
        '''Log Record Interface
        
        Log a record to file/stdout/Oakgate Console Output.
        
        Args:   
            logString : String to log to file
        Returns:
            None
        '''
        if None != self.logfileOperator:
            print(self.GetLocalTimeStringStandard(), 
                  sys._getframe(1).f_code.co_name,
                  '\t', 
                  sys._getframe(1).f_lineno,
                  logString, 
                  file = self.logfileOperator)
            #self.LoggingService.LogConsoleOutput(self.ConsoleLog_txt_FileObject, logString)
        else:
            print("Error: None type of log file operator!", 
                  sys._getframe(1).f_code.co_name, 
                  '\t', 
                  sys._getframe(1).f_lineno,
                  self.logfileOperator)
            #self.LoggingService.LogConsoleOutput(self.ConsoleLog_txt_FileObject, logString)
        if True == LOG_DEBUG:
            print(self.GetLocalTimeStringStandard(), 
                  sys._getframe(1).f_code.co_name, 
                  '\t', 
                  sys._getframe(1).f_lineno,
                  logString)
        
    def GetLocalTimeString(self):
        '''Get Local Time String
        
        Get Local Runtime TimeStamp.
        
        Args:
            None
        Returns:
            TimeStampString : String of TimeStamp
        '''
        return (time.strftime('%Y-%m-%d-%X', time.localtime(time.time())).replace(";", "-")).replace(":", "")
    
    def GetLocalTimeStringStandard(self):
        '''Get Local Time String Standard
        
        Get Local Runtime TimeStamp Standard.
        
        Args:
            None
        Returns:
            TimeStampString : String of TimeStamp
        '''
        return time.strftime('%Y-%m-%d-%X', time.localtime(time.time())).replace(";", "-")
    
    def DeInitialize(self):
        '''De-Initialize Log
        
        DeInitialize Log Module.
        
        Args:
            None
        Returns:
            None
        '''
        self.logfileOperator.close()
        #print("DeInitialize Done!")
 
if __name__ == "__main__":
    
    logPath = r"D:\04_py_project\07_exerciser\oagate_demo\oakgate_demo\src\Log_output"
    logFileName = "default-test.log"
    #print(help(LOG_API))
    logApi = LOG_API(logPath, logFileName)
    logApi.Log("test string:", " a", " b")
    logApi.Log("test string:", 5, b'233445f0')
    logApi.DeInitialize()
    