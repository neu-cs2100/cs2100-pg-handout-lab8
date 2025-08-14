import sys
sys.path.append("/path/to/this/directory") # Fill in this path
from q1 import Clothing

"""
Cotton clothes shrink in the dryer.
Please implement the dry() function below according to the comments. You will need to write documentation.
Don't forget the path above.
"""

def dry(clothes: list[Clothing]) -> None:
    # Iterate through the clothes which are passed to the argument, and if any are 
    # made of cotton, it should print a message saying that it shrank that clothing item.
    # Tip: override __str__() in the Clothing classes.
    pass


def main() -> None:
    # Create a list of clothing and pass it to dry()
    pass

if __name__ == '__main__':
    main()
