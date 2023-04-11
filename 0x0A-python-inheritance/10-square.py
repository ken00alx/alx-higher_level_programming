#!/use/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
Module with class BaseGeometry
"""

class square(Rectangle):
    """Square class that inherits from Regtangle that
    inherits BaseGeomery"""

    def __init__(self, size):
        """"Method for initialize attributes"""

        super().__init__(size, size)

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Rectangle area"""

        return self.__size ** 2
