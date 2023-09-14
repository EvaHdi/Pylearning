#coding: utf-8
import os
import lxml.etree as ET


from library.LOG_API import LOG_API
    
'''
@Functions  : XML file Access APIs for Oakgate
@Author     : Peter.Sun@longsys.com
@ChangeList : 
                @2022/6/23 <Version 1.0> -- Add Initial XML Read/Write Operation API.
'''

class XML_API():
    ''' XML API
    
    XML APIs
        Read/Write XML files.
    
    Key Methods:
        ReadAll
        WriteAll
        
    Attributes:
        None
    '''
    def __init__(self, fileName,log):
        '''Init XML_API Class
        
        Initialize XML API Class.
        
        Args:
            fileName : JSON File Name
        Returns:
        '''
        # self.log = LOG_API()
        # self.log.logging_info("Initialize of JSON_API...")
        self.log = log
        self.xml_file_name = fileName
        self.log.logging_info("xml_file_name is : {}".format(self.xml_file_name))
        self.parser = ET.XMLParser(strip_cdata=False)
        self.tree = ET.parse(self.xml_file_name, self.parser)
        self.root = self.tree.getroot()

    def SearchKeyList(self, key_name_list):
        '''SearchKeyList
        
        Search xml with key list that contains chain of key from root layer to deepest layer.
        
        Args:
            key_name_list : all key chain list to be searched
        Returns:
            xml_obj         : Object of value
        '''
        xml_obj = None
        for key in key_name_list:
            if None == xml_obj:
                search_obj = self.root
            else:
                search_obj = xml_obj
            xml_obj = search_obj.find(key)
        return xml_obj

    def ReadKeyTree(self, key_name_list = ["SvTestSet", 
                                           "SvTest", 
                                           "SvLunPath", 
                                           "lunSettings"
                                           ]
                    ):
        '''ReadKeyTree
        
        Read xml with key list that contains chain of key from root layer to deepest layer.
        
        Args:
            key_name_list : all key chain list to be searched
        Returns:
            status          : True=Read success; False=Read failure
            xml_obj         : Object of value
        '''
        self.log.logging_info("key list to search in xml: {}".format(key_name_list))

        xml_obj = self.SearchKeyList(key_name_list)
        # self.log.logging_info("xml_obj.tag={} text={} methods={}".format(
        #                                         xml_obj.tag, 
        #                                         xml_obj.text,
        #                                         dir(xml_obj)
        #                                       ))
        if None == xml_obj:
            return False, ""
        return True, xml_obj.text
                
    def UpdateKeyTree(self, key_name_list = ["SvTestSet", 
                                             "SvTest", 
                                             "SvLunPath", 
                                             "lunSettings"], 
                            new_text = "new text for test"
                    ):
        '''UpdateKeyTree
        
        Update xml with key text to last key of key list (deepest layer).
        
        Args:
            key_name_list   : all key chain list to be searched
            new_text        : new text to update to key
        Returns:
            status          : True=Update success; False=Update failure
        '''
        self.log.logging_info("key list to search in xml: {}".format(key_name_list))

        xml_obj = self.SearchKeyList(key_name_list)
            
        if None == xml_obj:
            return False
        else:
            xml_obj.text = new_text
            #self.log.logging_info("new_text = {}".format(new_text))
            return True
        
    def SaveXML(self, new_file_name = None):
        '''UpdateKeyTree
        
        Update xml with key text to last key of key list (deepest layer).
        
        Args:
            new_file_name   : new xml file name, default same with opened xml
        Returns:
            status          : True=Save success; False=Save failure
        '''
        if None == new_file_name:
            xml_file_name = self.xml_file_name
        else:
            xml_file_name = new_file_name
        if not os.path.isfile(new_file_name):
            self.log.logging_error("the file is not exist")

        self.tree.write(xml_file_name)


        return True
  
    def DeInitialize(self):
        '''De-Initialize XML_API
        
        DeInitialize XML API Module.
        
        Args:
            None
        Returns:
            None
        '''
        pass
        # self.log.DeInitialize()
        
if __name__ == "__main__":
    xmlFileName = "./AutomationFiles/GenericAutomationTemplate.at4"
    xmlApi = XML_API(fileName = xmlFileName)
    key_name_list = [   "SvTestSet", 
                        "SvTest", 
                        "SvLunPath", 
                        "lunSettings"]
    readkey_status, key_text = xmlApi.ReadKeyTree(key_name_list=key_name_list)
    xmlApi.UpdateKeyTree(key_name_list=key_name_list, new_text="text for test")
    xmlApi.SaveXML(new_file_name="./AutomationFiles/newTest.xml")
    xmlApi.DeInitialize()
    