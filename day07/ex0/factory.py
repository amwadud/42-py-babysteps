from abc import ABC, abstractmethod

from .creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature: ...

    @abstractmethod
    def create_evolved(self) -> Creature: ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from .creature import Flameling

        return Flameling("Flameling")

    def create_evolved(self) -> Creature:
        from .creature import Pyrodon

        return Pyrodon("Pyrodon")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from .creature import Aquabub

        return Aquabub("Aquabub")

    def create_evolved(self) -> Creature:
        from .creature import Torragon

        return Torragon("Torragon")
