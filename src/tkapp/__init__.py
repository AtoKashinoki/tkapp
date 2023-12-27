"""
    TkApp module

Can be used to create window application.
"""


# import support modules
import sys


""" self status """


__self_name__ = "tkapp"


""" check execute file """


if not __name__ == __self_name__:
    print("**Not import self**")
    sys.exit()


""" Initialize self process """


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


try:
    import tkapp.descriptor as descriptor
except (ImportError, OSError) as e:
    descriptor = ImportMissing("descriptor", e)


print("**Initialized tkapp module**")
