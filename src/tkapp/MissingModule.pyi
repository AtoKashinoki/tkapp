"""
    Import missing class.
"""


import_missing_errors: tuple[type[ImportError], type[OSError]]


class ImportMissing:
    __name: str
    __message: str
    __error_modules: dict[str, str]
    def __init__(self, package_name: str, message: str): ...
    def __repr__(self) -> str: ...
    @staticmethod
    def errors() -> dict[str, str]: ...
