"""BaseGeometry class (Integer_Validator)"""
class BaseGeometry:
    def area(self):
        """This raises an Exception error if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value passed in.
        If the value is not an integer, 
           A TypeError exception is raised
        If the value is less than or equal to 0, 
           A ValueError exception is raised."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            
            raise ValueError(f"{name} must be greater than 0")


"""instanciation"""
myobject = BaseGeometry()
print(dir(myobject))