"""
    File to define BaseException
"""


class BaseException(Exception):
    """class BaseException to define the base custom exception.

        Attributes:
            message (str): message for the exception
    """

    def __init__(self, message: str) -> None:
        """Initializes the BaseException with message.

        Args:
            message (str): message for the exception
        """
        super().__init__(message)
        self.__message: str = message

    def __str__(self) -> str:
        """Get BaseException representation 

        Returns:
            str: BaseException representation 
        """
        return self.__message
