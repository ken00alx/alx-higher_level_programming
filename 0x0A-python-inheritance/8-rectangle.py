#!/usr/bin/python3
BaseGeomtry = __import__('7-base_geometry').BaseGeometry

"""module rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle, inherited from class
    BaseGeometry"""

    def __init__(self, with, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
