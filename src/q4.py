"""
Please implement the classes ClothingStoreItem and Purchasable below according to the comments. You will need to write documentation.
"""

from typing import TypeVar, Generic


class ClothingStoreItem:
    # Represents an item on a rack at a clothing store
    # It should have three properties:
    # 1: The price of the item in cents (an int)
    # 2: Whether it is for adults (as opposed to children) (a bool)
    # 3: The item itself (generic, but it must be a type of Clothing)

    def __str__(self) -> str:
        # Return a string that includes what the item is, and its price (e.g., "cotton shirt which costs $10.35").
        pass


# Stores like Costco and Target have many departments, of which clothing is one.
# The only thing that all the items have in common is that they have a price.

T = TypeVar("T")


class Purchasable(Generic[T]):
    # Two properties:
    # 1: the price in cents (an int)
    # 2: the item itself (generic T)
    pass


# Modify ClothingStoreItem so that it extends Purchasable.
# You may need to move ClothingStoreItem so that it is below Purchasable in the file.


# Create another class called FoodStoreItem which is Purchasable.
