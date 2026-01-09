import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f"Error occurred in script: {self.filename} at line number: {self.lineno} with message: {self.error_message}".format(self.filename,self.lineno,str(self.error_message))
    

        

