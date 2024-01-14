"""
    Descriptor classes
"""

from abc import ABC


class Skeleton(ABC):
    __owner: object
    __name: str
    def __set_name__(self, owner: object, name: str) -> None: ...
    @property
    def owner(self) -> object: ...
    @property
    def name(self) -> str: ...
    def __set__(self, instance: object, owner: object) -> None: ...
    def __get__(self, instance: object, owner: object) -> None: ...