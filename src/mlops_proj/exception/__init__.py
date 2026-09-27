import sys
import logging
from typing import Any


def error_message_detail(error: str, error_detail: Any) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in python script: [{file_name}] "
        f"at line number [{line_number}]: {error}"
    )

    logging.error(error_message)
    return error_message


class MyException(Exception):
    """
    Custom exception class.
    """

    def __init__(self, error_message: str, error_detail: Any):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message