"""
   tkapp.descriptor.Skeleton

This file describe Skeleton class of descriptor.
"""


# import abc module
from abc import ABC


class Skeleton(ABC):
    """
        Descriptor skeleton class.

    This class is inheritance class.
    Can be used to create descriptor classes.
    """

    def __set_name__(self, owner, name) -> None:
        """ Create descriptor """
        self.__owner, self.__name = owner, name
        return

    @property
    def owner(self) -> object:
        """ Return owner class """
        return self.__owner

    @property
    def name(self) -> str:
        """ Return attribute name """
        return self.__name

    def __set__(self, instance: object, value: any) -> None:
        """ Set values """
        instance.__dict__[self.__name] = value
        return

    def __get__(self, instance: object, owner: object) -> any:
        """ Get values """
        return instance.__dict__[self.__name]
