
# errors when import packages
import_missing_errors = (ImportError, OSError)


# Import missing class
class ImportMissing:
    """
        ImportMissing class.

    This class is used on import errors.
    """

    def __init__(self, package_name: str, error_message):
        """
            Register package name and error message.
        :param package_name: Package name.
        :param error_message: Error message when import package.
        """
        self.__name = package_name
        self.__message = error_message
        return

    def __repr__(self):
        return f"ImportError: {self.__name} -> {self.__message}"
