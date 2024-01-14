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


# ImportMissing class
try:
    from tkapp.MissingModule import (
        ImportMissing,
        import_missing_errors,
    )
except (ImportError, OSError) as message:
    raise ImportError(message)


# Error classes


try:
    import tkapp.Error
except import_missing_errors as message:
    Error = ImportMissing("Error", message)


print("**Initialized tkapp module**")
