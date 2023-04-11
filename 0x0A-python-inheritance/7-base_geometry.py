#!/use/bin/python3
"""
Module with class BaseGeometry
""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
    """Method for calculated area"""
    raise Exception("area() is not implemente")

    def integer_validator(self, name, value):
        """ Method for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be in integer".format(name))
        if value <= 0:
            raise valueError("{} must be greater than 0.".format(name))
