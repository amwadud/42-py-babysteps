from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str: ...


class TransformCapability(ABC):
    _is_transformed: bool

    def __init__(self) -> None:
        self._is_transformed = False

    @abstractmethod
    def transform(self) -> str: ...

    @abstractmethod
    def revert(self) -> str: ...
