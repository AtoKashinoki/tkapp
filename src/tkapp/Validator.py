"""
    tkapp.Validator

This file describe Validator classes.
"""


# import modules
from abc import ABC, abstractmethod
from tkapp.Descriptor import Skeleton as DescriptorSkeleton


""" Skeleton """


class Skeleton(DescriptorSkeleton, ABC):
    """
        Validator skeleton class.

    This class is inheritance class.
    Can be used to create Validator classes.
    """

    def __set__(self, instance, value) -> None:
        self.validate(instance, value)
        DescriptorSkeleton.__set__(self, instance, value)
        return

    @abstractmethod
    def validate(self, instance, value) -> None:
        """
            Validation method
        """
        return


""" Descriptor Validators """

""" Data type validator """


# validate data type


def validate_data_types(data, validates):
    """ Validate data type """
    if any in validates:
        return

    if data is None and None in validates:
        return
    if type(data) in validates:
        return

    raise TypeError(f"This value type cannot be assigned: {type(data)}('{data}')\n"
                    f"-> Types can use: {validates}")


class DataType(Skeleton):
    """
        Data type validator class.

    This class is descriptor class that validate data type.
    """

    def __init__(self, *validate_data_types, mode="wr"):
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

    def validate(self, instance, value) -> None:
        """ Validate data type """
        # disable
        if self.__disable_validation:
            self.__disable_validation = False
            return

        # mode
        if "w" not in self.__mode and self.name in instance.__dict__.keys():
            raise TypeError(f"non-writable mode")

        # validate
        validate_data_types(value, self.__validate_data_types)
        return

    def __get__(self, *args) -> any:
        # mode
        if "r" not in self.__mode:
            raise TypeError(f"non-readable mode")

        # get value
        return Skeleton.__get__(self, *args)


""" Attribute validator """


# validate attribute


def validate_attributes(value, attributes):
    """ Validate attributes """
    for attribute in attributes:
        if attribute in value.__attributes__:
            return
        continue

    raise TypeError(f"This value attribute cannot be assigned: {type(value)}('{value.__attributes__}')\n"
                    f"-> Attributes can use: {attributes}")


class Attribute(DataType):
    """
        Attribute validator class.

    This class is descriptor class that validate attribute.
    """

    def __init__(self, *attributes: str, mode="rw"):
        """
            Initialize validate attribute and set mode.

        mode ->
            wr: Self can set and get values.

            r: Self can initialize and get values.

        :param attributes: Attribute to register.
        :param mode: Self mode. (default: "wr")
        """
        super().__init__(any, mode=mode)
        self.__validate_attributes = attributes
        return

    @property
    def validate_attributes(self):
        """ Return validate attributes """
        return self.__validate_attributes

    def validate(self, instance, value) -> None:
        """ Validate attribute """
        # data type
        DataType.validate(self, instance, value)

        # attribute
        validate_attributes(value, self.__validate_attributes)
        return


""" Container Validators """

""" Data type """


class DataTypeDict(dict):
    """
        DataType dict class

    This class is dict class that validate data types.
    """

    def __init__(
            self,
            *value_validate_data_types,
            key_validate_data_types=(str, tuple),
            initial_values=None, mode="wr"
    ):
        """
            Initialize self and values.

        mode ->
            wr: Self can set and get values.

            r: Self can initialize and get values.

        :param value_validate_data_types: Value of data type to register.
        :param key_validate_data_types: Key of data type to register.
        :param initial_values: initial value of self.
        :param mode: Self mode. (default: "wr")
        """
        self.__value_validate_data_type = value_validate_data_types
        self.__key_validate_data_type = key_validate_data_types
        self.__mode = mode
        self.__disable_validation = False
        dict.__init__(self)

        [self.__setitem__(*items) for items in initial_values.items()]
        return

    def disable_only_once(self):
        """ Disable validation method only once """
        self.__disable_validation = True
        return

    def __setitem__(self, key, value):
        self.validate(key, value)
        dict.__setitem__(self, key, value)
        return

    def validate(self, key, value):
        """ validate data types """
        # disable
        if self.__disable_validation:
            self.__disable_validation = False
            return

        # mode
        if "w" not in self.__mode:
            raise TypeError(f"non-writable mode")

        # validate
        datas = [key, value]
        validates = [self.__key_validate_data_type, self.__value_validate_data_type]
        [validate_data_types(*args) for args in zip(datas, validates)]
        return


""" Attribute """


class AttributeDict(DataTypeDict):
    """
        Attribute validator dict

    This class is container class that validate attributes.
    """

    def __init__(
            self,
            *attributes,
            key_validate_data_types=(str, tuple),
            initialize_values=None,
            mode="rw"
    ):
        """
            Initialize validate attribute and set mode.

        mode ->
            wr: Self can set and get values.

            r: Self can initialize and get values.

        :param attributes: Attribute to register.
        :param key_validate_data_types: Key of data type to register.
        :param initial_values: initial value of self.
        :param mode: Self mode. (default: "wr")
        """
        self.__validate_attributes = attributes
        super().__init__(
            any,
            key_validate_data_types=key_validate_data_types,
            initial_values=initialize_values,
            mode=mode
        )
        return

    @property
    def validate_attributes(self):
        """ Return validate attributes """
        return self.__validate_attributes

    def validate(self, key, value) -> None:
        """ Validate attribute """

        # data type
        DataTypeDict.validate(self, key, value)

        # attribute
        validate_attributes(value, self.__validate_attributes)
        return
