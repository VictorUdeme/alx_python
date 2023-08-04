"""BaseGeometry class"""
class BaseGeometry:
    def area(self):
        """This raises an Exception error if area is not implemented"""
        raise Exception("area() is not implemented")



"""instanciation"""
myobject = BaseGeometry()
print(dir(myobject))