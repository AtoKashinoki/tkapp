"""
    tkapp.error

This file packages classes about error used by tkapp.
"""


# ImportMissingClass
try:
    from tkapp.error.MissingClass import (
        ImportMissing,
        import_missing_errors,
    )
except (ImportError, OSError) as message:
    raise ImportError(message)


# Error classes
try:
    from tkapp.error import ErrorClasses
except import_missing_errors as message:
    ErrorClass = ImportMissing("ErrorClass", message)
