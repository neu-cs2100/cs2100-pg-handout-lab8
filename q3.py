import sys
sys.path.append("/path/to/this/directory") # Fill in this path
from q1 import Clothing

from typing import TypeVar, Generic

# Have you ever lost a button and replaced it with a paperclip? 
# Or rubber duck? Shirts can use almost anything as a button.

B = TypeVar('B')

class Shirt(Generic[B], Clothing):
    # Give the Shirt class a property which is a list of buttons.
    # Shirts can use anything as a button, so the buttons in this list are of type B (generic).
    # We are stylish, so all the buttons on the shirt must be the same type as each other.
    pass


def main() -> None:
    # Create a list of Shirts.
    # What sort of weird items can you use as a button?
    # Can you use pants as a button? What about a Spider?
    pass

if __name__ == '__main__':
    main()
