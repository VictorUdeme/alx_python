"""BaseGeometry class"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")



"""instanciation"""
myobject = BaseGeometry()
print(dir(myobject))