from abc import ABC, abstractmethod

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



# Create two classes which implement the Clothing interface.
# Examples include Shirt, Pants, and Scarf.
