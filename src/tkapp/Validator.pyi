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

class DataType(Validator.Skeleton):
    __validate_data_types: tuple[any, ...]
    __mode: str
    __disable_validation: bool
    def __init__(self, *validate_data_types: Union[type, None] or any, mode: str): ...
    @property
    def validate_data_type(self) -> tuple[any]: ...
    @property
    def mode(self) -> str: ...
    def disable_only_once(self) -> None: ...
    def validate(self, instance: object, value: any) -> None: ...
    def __get__(self, instance: object, owner: object): ...

class Attribute(DataType):
    __validate_attribute: tuple[str, ...]
    def __init__(self, attribute: str, mode: str): ...
    @property
    def validate_attributes(self) -> tuple[str, ...]: ...
    def validate(self, instance: object, value: any) -> None: ...
