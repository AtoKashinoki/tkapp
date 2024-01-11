"""
    tkapp.descriptor

This file packages descriptor classes used by tkapp.
"""


# ImportMissing class
try:
    from tkapp.error.MissingClass import (
        ImportMissing as _ImportMissing,
        import_missing_errors as _import_errors,
    )
except (ImportError, OSError) as message:
    raise ImportError(message)


# Skeleton class
try:
    from tkapp.descriptor.Skeleton import Skeleton
except _import_errors as message:
    Skeleton = _ImportMissing("descriptor.Skeleton", message)
