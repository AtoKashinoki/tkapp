"""
    Validator classes.
"""

from typing import Union
from abc import ABC, abstractmethod

import Descriptor


class Skeleton(Descriptor.Skeleton, ABC):
    def __set__(self, instance: object, value: any) -> None: ...
    @abstractmethod
    def validate(self, instance: object, value: any) -> None: ...

class Validator:
    Skeleton = Skeleton

def validate_data_types(data: any, validates: type[any]) -> None: ...

class DataType(Validator.Skeleton):
    __validate_data_types: tuple[any, ...]
    __mode: str
    __disable_validation: bool
    def __init__(self, *validate_data_types: Union[type, None] or any, mode: str = "wr"): ...
    @property
    def validate_data_type(self) -> tuple[any]: ...
    @property
    def mode(self) -> str: ...
    def disable_only_once(self) -> None: ...
    def validate(self, instance: object, value: any) -> None: ...
    def __get__(self, instance: object, owner: object): ...

def validate_attributes(value: any, attributes: tuple[str, ...]): ...

class Attribute(DataType):
    __validate_attributes: tuple[str, ...]
    def __init__(self, *attribute: str, mode: str = "wr"): ...
    @property
    def validate_attributes(self) -> tuple[str, ...]: ...
    def validate(self, instance: object, value: any) -> None: ...

class DataTypeDict(dict):
    __value_validate_data_type: tuple[any, ...]
    __key_validate_data_type: tuple[any, ...]
    __mode: str
    __disable_validation: bool
    def __init__(
            self,
            *value_validate_data_types: Union[type, None] or any,
            key_validate_data_types: tuple[Union[type, None] or any] = (str, tuple),
            initial_values: dict[any, any] = None,
            mode: str = "wr"
    ): ...
    def disable_only_once(self) -> None: ...
    def validate(self, key: any, value: any) -> None: ...


class AttributeDict(DataTypeDict):
    __validate_attributes: tuple[str, ...]
    def __init__(
            self,
            *attributes: str,
            key_validate_data_types: tuple[Union[type, None] or any]=(str, tuple),
            initialize_values: dict[any, any] = None,
            mode: str = "rw"
    ): ...
    def validate_attributes(self) -> tuple[str, ...]: ...
    def validate(self, key: any, value: any) -> None: ...
