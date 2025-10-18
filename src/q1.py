from abc import ABC, abstractmethod

"""
Please implement the Clothing abstract base class according to the comments describing its functionality.
It will have abstract aspects which are implemented by concrete subclasses.

Then, create two classes which implement the Clothing interface.
Examples include Shirt, Pants, and Scarf.
"""

class Clothing(ABC):
    # Interface for Clothing. All of its methods should be abstract.
    @property
    @abstractmethod
    def color(self) -> str:
        # Abstract property that must be implemented by concrete subclasses
        pass

    @property
    @abstractmethod
    def material(self) -> str:
        # Abstract property that must be implemented by concrete subclasses
        pass


