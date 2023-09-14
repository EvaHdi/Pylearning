'''
@Functions  : Print Format time 
@Author     : hobart.chen@longsys.com
@ChangeList : 
                @2023/3/20 <Version 1.0> -- Add Format Time API
'''

import time

class TIME_API():
    # def __init__(self):
        
    #format ####-#-## ##:##:##       
    def getlocaltimeString(self):
        '''
        Get Local Runtime TimeStamp.
        Args:
            None
        Returns:
            TimeStampString : String of TimeStamp
        '''
        return   time.strftime('%Y-%m-%d %X', time.localtime(time.time())).replace(";", "-")

