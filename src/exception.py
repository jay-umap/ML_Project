import sys
from src.logger import logging

# Configure logging (ensure logs are captured properly)
logging.basicConfig(
    filename="error.log", 
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

def error_message_detail(error, error_detail: sys):
    """
    Extracts error details including filename and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename    
    error_message = "Error occurred in script name [{0}], line number[{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
        

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class for detailed error reporting.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
          # Correctly initializing Exception class
    
    def __str__(self):
        return self.error_message

