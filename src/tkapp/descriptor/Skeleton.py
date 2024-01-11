"""
   tkapp.descriptor.Skeleton

This file describe Skeleton class of descriptor.
"""


# import abc module
import abc


class Skeleton(abc.ABC):
    """
        Descriptor skeleton class.

    This class is inheritance class.
    Can be used to create descriptor classes.
    """

    def __set_name__(self, owner: object, name: str) -> None:
        """"""
        self.__owner, self.__name = owner, name
        return

    @property
    def owner(self) -> object:
        """ owner class """
        return self.__owner

    @property
    def name(self) -> str:
        """ attribute name """
        return self.__name

    def __set__(self, instance: object, value: any) -> None:
        """ Set values """
        instance.__dict__[self.__name] = value
        return

    def __get__(self, instance: object, owner: object) -> any:
        """ Get values """
        return instance.__dict__[self.__name]
