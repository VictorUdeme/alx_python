"""
The Class module
"""


class BaseGeometry:
    def area(self) -> int:
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    def __init__(self, width: int, height: int) -> None:
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name: str, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self) -> int:
        return self.__width * self.__height

    def __str__(self) -> str:
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self) -> str:
        return f"Rectangle({self.__width}, {self.__height})"


class Square(Rectangle):
    def __init__(self, size: int) -> None:
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self) -> int:
        return self.__size * self.__size