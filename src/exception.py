import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() 
    
    '''
    .exc_info() returns a tuple containing:
    1. Exception Type (ignored with _)
    2. Exception Value (ignored with _)
    3. Traceback Object (exc_tb) → Contains details about where the error occurred.

    '''

    file_name = exc_tb.tb_frame.f_code.co_filename

    ''' 

    1.  exc_tb.tb_frame: Retrieves the frame where the error happened.
    2.  .f_code.co_filename: Extracts the script file name where the error occurred.

    '''

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)   # Calls the parent Exception class constructor.
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self): 
        return self.error_message
    
    ''' 
     When an object of CustomException is printed, it returns the formatted error message.
    '''