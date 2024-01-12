"""
    tkapp.descriptor.Validator

This file describe Validator classes.
"""


# import abc
from abc import ABC, abstractmethod


# import descriptor skeleton class
from tkapp.descriptor.Skeleton import Skeleton as DescriptorSkeleton


""" Skeleton """


class Skeleton(DescriptorSkeleton, ABC):
    """
        Validator skeleton class.

    This class
    """

    def __set__(self, instance, value) -> None:
        self.validate(instance, value)
        DescriptorSkeleton.__set__(self, instance, value)
        return

    @abstractmethod
    def validate(self, instance: object, value: any) -> None:
        """
            Validation method
        """
        return


""" Data type validator """


class DataType(Skeleton):
    """
        Data type validator class.

    This class is descriptor class that validate data type.
    """

    def __init__(self, *validate_data_types: type or None or any, mode: str = "wr"):
        """
            Initialize validate data types and set mode.

        mode ->
            wr: Self can set and get values.

            r: Self can initialize and get values.

        :param validate_data_types: Data type to register.
        :param mode: Self mode. (default: "wr")
        """
        self.__validate_data_types = validate_data_types
        self.__mode = mode
        self.__disable_validation: bool = False
        return

    @property
    def validate_data_types(self):
        """ Return validate data types """
        return self.__validate_data_types

    @property
    def mode(self):
        """ Return mode """
        return self.__mode

    def disable_only_once(self):
        """ Disable validation method only once """
        self.__disable_validation = True
        return

    def validate(self, instance: object, value: any) -> None:
        """ Validate data type """
        # disable
        if self.__disable_validation:
            self.__disable_validation = False
            return

        # mode
        if "w" not in self.__mode and self.name in instance.__dict__.keys():
            raise TypeError(f" pass write mode ")

        # validate
        if any in self.__validate_data_types:
            return

        if value is None and None in self.__validate_data_types:
            return
        if type(value) in self.__validate_data_types:
            return

        raise TypeError(f" pass type ")

    def __get__(self, *args) -> any:
        # mode
        if "r" not in self.__mode:
            raise TypeError(f" pass read mode ")

        # get value
        return Skeleton.__get__(self, *args)


""" Attribute validator """


class Attribute(DataType):
    """
        Attribute validator class.

    This class is descriptor class that validate attribute.
    """

    def __init__(self, *attributes: str, mode: str = "rw"):
        """
            Initialize validate attribute and set mode.

        mode ->
            wr: Self can set and get values.

            r: Self can initialize and get values.

        :param attributes: Attribute to register.
        :param mode: Self mode. (default: "wr")
        """
        DataType.__init__(self, any, mode=mode)
        self.__validate_attributes = attributes
        return

    @property
    def validate_attributes(self):
        """ Return validate attributes """
        return self.__validate_attributes

    def validate(self, instance: object, value: any) -> None:
        """ Validate attribute """
        # data type
        DataType.validate(self, instance, value)

        # attribute
        print(value.__class__.__dict__)

        for attribute in self.__validate_attributes:
            if attribute in value.__attributes__:
                return
            continue

        raise TypeError(f" pass attribute ")
