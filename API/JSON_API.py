#coding: utf-8

'''
@Functions  : Json file Access APIs for Oakgate
@Author     : Peter.Sun@longsys.com
@ChangeList : 
                @2022/6/23 <Version 1.0> -- Add Initial JSON Read/Write Operation API
'''

import os,time,sys
import json

try:
    from library.LOG_API import LOG_API
except:
    from LOG_API import LOG_API
    
class JSON_API():
    ''' JSON_API
    
    JSON APIs
        Read/Write JSON files.
    
    Key Methods:
        ReadAll
        writeall
        
    Attributes:
        None
    '''
    def __init__(self, fileName ,log):
        '''Init JSON_API Class
        
        Initialize JSON_API Class.
        
        Args:
            fileName : JSON File Name
        Returns:
        '''
        # self.log = LOG_API()
        # self.log.logging_info("Initialize of JSON_API...")
        self.log = log 
        self.json_file_name = fileName
        
    def ReadAll(self):
        json_content = {}
        
        # if False == os.path.isfile(self.json_file_name):
        #     return json_content
        
        with open(self.json_file_name, "r+") as fr:
            json_content = json.load(fr)
            
        return json_content

    def writeall(self, json_content = {}):
        
        # if False == os.path.isfile(self.json_file_name):
        #     return False
        self.log.logging_info("self.json_file_name={}".format(self.json_file_name))
        with open(self.json_file_name, "w") as fw:
            json.dump(json_content, fw)
            
        return True
    
    def DeInitialize(self):
        '''De-Initialize JSON API
        
        DeInitialize JSON API Module.
        
        Args:
            None
        Returns:
            None
        '''
        pass
        # self  .log.DeInitialize()
        