"""
    tkapp.MissingModule

This file describe ImportMissing class and errors variables.
"""
# errors when import packages
import_missing_errors = (ImportError, OSError)


# Import missing class
class ImportMissing:
    """
        ImportMissing class.

    This class is used on import errors.
    """
    __error_modules = {}

    def __init__(self, package_name, message):
        """
            Register package name and error message.
        :param package_name: Package name.
        :param message: Error message when import package.
        """
        self.__name = package_name
        self.__message = message
        ImportMissing.__error_modules[package_name] = message
        return

    @staticmethod
    def errors():
        return ImportMissing.__error_modules

    def __repr__(self):
        return f"ImportError: {self.__name} -> {self.__message}"
