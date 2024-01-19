"""
    tkapp.Widget

This file describe widget classes.
"""


# import modules
from abc import ABC, abstractmethod
from tkapp.Validator import DataType


""" Skeleton class """


class Skeleton(ABC):
    """
        Widget.Skeleton class

    This class is inheritance class.
    Can be used to create Widget classes.
    """
    __attributes = DataType(tuple)

    def __init__(self, attributes):
        """"""
        self.__attributes = attributes
        return

    @property
    def __attributes__(self) -> tuple[str]:
        """ Return attributes """
        return self.__attributes
